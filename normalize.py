from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# Optional: faster/better fuzzy matching if you have it.
try:
    from rapidfuzz import fuzz  # type: ignore
    _HAS_RAPIDFUZZ = True
except Exception:
    _HAS_RAPIDFUZZ = False
    import difflib


_ROMAN_RE = re.compile(r"^(?=[IVXLCDM]+$)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", re.I)
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+", re.I)
_WS_RE = re.compile(r"\s+")

# Feel free to tweak: stopwords to keep lowercase in Title Case output.
_TITLE_STOPWORDS = {"and", "or", "the", "of", "a", "an", "to", "in", "on", "for", "vs", "v", "with"}


def _is_roman(s: str) -> bool:
    s = s.strip().upper()
    return bool(s) and bool(_ROMAN_RE.match(s))


def _arabic_to_roman(n: int) -> str:
    # Enough for game sequels; expand if you want.
    if not (0 < n < 4000):
        return str(n)
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    out = []
    for v, sym in vals:
        while n >= v:
            out.append(sym)
            n -= v
    return "".join(out)


def _normalize_key(term: str) -> str:
    """
    Aggressive key for matching: lowercased, punctuation collapsed,
    spaces collapsed, roman numerals & digits retained (not converted).
    """
    t = term.strip()
    t = t.replace("&", " and ")
    t = _WS_RE.sub(" ", t)
    t = t.lower()

    # Keep spaces for token comparisons, but normalize punctuation to space.
    t = _NON_ALNUM_RE.sub(" ", t)
    t = _WS_RE.sub(" ", t).strip()
    return t


def _tokens(term: str) -> List[str]:
    key = _normalize_key(term)
    return key.split() if key else []


def _simple_singularize(word: str) -> str:
    """
    Very light plural handling. This is *not* full NLP.
    """
    w = word
    if len(w) <= 3:
        return w
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith("es") and len(w) > 4:
        return w[:-2]
    if w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def _title_case_preserve_roman(s: str) -> str:
    """
    Title-case words, but keep roman numerals uppercase.
    """
    parts = re.split(r"(\s+)", s.strip())
    out = []
    for p in parts:
        if p.isspace() or p == "":
            out.append(p)
            continue
        raw = p
        # Strip punctuation around word for roman check, but keep punctuation in output.
        m = re.match(r"^([^A-Za-z0-9]*)([A-Za-z0-9]+)([^A-Za-z0-9]*)$", raw)
        if not m:
            out.append(raw)
            continue
        pre, core, post = m.group(1), m.group(2), m.group(3)
        if _is_roman(core):
            core_out = core.upper()
        else:
            low = core.lower()
            if low in _TITLE_STOPWORDS:
                core_out = low
            else:
                core_out = low[:1].upper() + low[1:]
        out.append(pre + core_out + post)

    # If first token was a stopword, capitalize it anyway.
    joined = "".join(out).strip()
    if joined:
        first_word = joined.split(" ", 1)[0]
        if first_word.lower() in _TITLE_STOPWORDS and not _is_roman(first_word):
            joined = first_word[:1].upper() + first_word[1:] + ("" if " " not in joined else " " + joined.split(" ", 1)[1])
    return joined


def _initialism(tokens: List[str]) -> str:
    """
    "EverQuest II" -> "EQII"
    Ignores stopwords and digits.
    """
    letters = []
    for tok in tokens:
        if tok in _TITLE_STOPWORDS:
            continue
        if tok.isdigit():
            continue
        letters.append(tok[0].upper())
    return "".join(letters)


def _sequels_variants(tokens: List[str]) -> List[str]:
    """
    Create a few common sequel variants for matching:
      - "eq2", "eq 2", "eqii", etc.
    """
    if not tokens:
        return []
    variants = []

    init = _initialism(tokens)
    if init:
        variants.append(init)

    # If last token is a digit, generate Roman variant and concatenations.
    if tokens and tokens[-1].isdigit():
        n = int(tokens[-1])
        roman = _arabic_to_roman(n)
        base = tokens[:-1]
        init_base = _initialism(base) if base else init
        if init_base:
            variants.extend([f"{init_base}{n}", f"{init_base}{roman}", f"{init_base} {n}", f"{init_base} {roman}"])

    # If last token is roman numeral, also generate digit variant.
    if tokens and _is_roman(tokens[-1]):
        # Convert roman to int (small, safe).
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        r = tokens[-1].upper()
        total = 0
        prev = 0
        for ch in reversed(r):
            val = roman_map.get(ch, 0)
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        base = tokens[:-1]
        init_base = _initialism(base) if base else _initialism(tokens)
        if init_base and total > 0:
            variants.extend([f"{init_base}{total}", f"{init_base} {total}"])

    # Also provide concatenated key (no spaces) for matching "eq2" vs "eq 2"
    variants.extend([
        "".join(tokens).lower(),
        " ".join(tokens).lower(),
    ])

    # Dedup
    seen = set()
    out = []
    for v in variants:
        vv = _WS_RE.sub(" ", v.strip())
        if vv and vv not in seen:
            seen.add(vv)
            out.append(vv)
    return out


def _similar(a: str, b: str) -> float:
    """
    Similarity score 0..1.
    """
    if _HAS_RAPIDFUZZ:
        # token_set_ratio is forgiving for word order and punctuation
        return fuzz.token_set_ratio(a, b) / 100.0
    else:
        return difflib.SequenceMatcher(None, a, b).ratio()


class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1


@dataclass
class NormalizerConfig:
    # Similarity threshold for clustering near-duplicates.
    similarity_threshold: float = 0.90
    # If you have lots of short tags like "AI", "RPG", tune down or handle separately.
    min_len_for_fuzzy: int = 5


def write_normalized_csv(
    input_csv_path: str | Path,
    output_csv_path: str | Path,
    *,
    # manual alias -> canonical (e.g., {"EQ2": "EverQuest II", "eq ii": "EverQuest II"})
    manual_map: Optional[Dict[str, str]] = None,
    config: NormalizerConfig = NormalizerConfig(),
    name_column_index: int = 2,  # New parameter to specify which column contains the names
    has_header: bool = True,     # New parameter to specify if CSV has header
) -> None:
    """
    Reads a CSV and normalizes the specified column (default: column 2 which is 'name'),
    writes a CSV with all original columns plus a new 'normalized_name' column.

    Handles:
      - case and punctuation normalization
      - "eq2"/"eq ii"/"EverQuest 2" style variants via initialisms + sequel handling
      - light plural/singular normalization
      - fuzzy clustering of near-duplicates
      - manual overrides via manual_map (recommended for best results)

    NOTE: This is heuristic. For perfect mappings, seed manual_map with your key franchises/series.
    """
    input_csv_path = Path(input_csv_path)
    output_csv_path = Path(output_csv_path)
    manual_map = manual_map or {}

    # Normalize manual keys for robust matching
    manual_key_to_canon: Dict[str, str] = {}
    for k, v in manual_map.items():
        manual_key_to_canon[_normalize_key(k)] = v
        # Also allow matching on "no-space" key and sequel variants
        toks = _tokens(k)
        for alt in _sequels_variants(toks):
            manual_key_to_canon[_normalize_key(alt)] = v

    # Read all rows, extracting terms from the specified column
    rows: List[List[str]] = []
    terms: List[str] = []
    header = None
    
    with input_csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        # Handle header if present
        if has_header:
            header = next(reader, None)
            if header:
                rows.append(header)
        
        for row in reader:
            if not row:
                continue
            rows.append(row)
            # Extract the name from the specified column, default to empty string if column doesn't exist
            name = row[name_column_index].strip() if len(row) > name_column_index else ""
            terms.append(name)

    # Skip header row for processing
    processing_rows = rows[1:] if has_header else rows
    processing_terms = terms[1:] if has_header else terms

    # Unique terms for clustering (only non-empty terms)
    unique_terms = sorted(set(t for t in processing_terms if t))
    if not unique_terms:
        # If no valid terms found, just copy the input
        print("No valid terms found to normalize.")
        return
        
    idx = {t: i for i, t in enumerate(unique_terms)}
    uf = UnionFind(len(unique_terms))

    # Build keys and variant indices for cheap unions (abbrev/sequel/plural)
    key_to_indices: Dict[str, List[int]] = {}
    for t in unique_terms:
        i = idx[t]
        k = _normalize_key(t)
        key_to_indices.setdefault(k, []).append(i)

        toks = _tokens(t)

        # plural/singular variant on last token
        if toks:
            toks_sing = toks[:-1] + [_simple_singularize(toks[-1])]
            if toks_sing != toks:
                key_to_indices.setdefault(" ".join(toks_sing), []).append(i)

        # sequel / initialism variants (eq2, eqii, etc.)
        for alt in _sequels_variants(toks):
            key_to_indices.setdefault(_normalize_key(alt), []).append(i)

    # Union exact-key buckets
    for inds in key_to_indices.values():
        if len(inds) > 1:
            base = inds[0]
            for j in inds[1:]:
                uf.union(base, j)

    # Apply manual map unions (everything that matches a manual key becomes that canonical cluster)
    # We do this by forcing terms that match a manual key to share a representative.
    canon_to_rep: Dict[str, int] = {}
    for t in unique_terms:
        i = idx[t]
        k = _normalize_key(t)
        if k in manual_key_to_canon:
            canon = manual_key_to_canon[k]
            rep = canon_to_rep.get(canon)
            if rep is None:
                canon_to_rep[canon] = i
            else:
                uf.union(rep, i)

        # Also check sequels variants for manual map hits
        toks = _tokens(t)
        for alt in _sequels_variants(toks):
            kk = _normalize_key(alt)
            if kk in manual_key_to_canon:
                canon = manual_key_to_canon[kk]
                rep = canon_to_rep.get(canon)
                if rep is None:
                    canon_to_rep[canon] = i
                else:
                    uf.union(rep, i)

    # Fuzzy union for near duplicates (limited to terms of reasonable length)
    # O(n^2) worst case; with 2.4k uniques it’s OK if we prune.
    # Prune by first letter bucket of normalized key to reduce comparisons.
    buckets: Dict[str, List[int]] = {}
    norm_keys = [_normalize_key(t) for t in unique_terms]
    for i, k in enumerate(norm_keys):
        lead = k[:1] if k else "#"
        buckets.setdefault(lead, []).append(i)

    for inds in buckets.values():
        # Compare within bucket only
        for a_pos in range(len(inds)):
            i = inds[a_pos]
            if len(norm_keys[i]) < config.min_len_for_fuzzy:
                continue
            for b_pos in range(a_pos + 1, len(inds)):
                j = inds[b_pos]
                if len(norm_keys[j]) < config.min_len_for_fuzzy:
                    continue
                if uf.find(i) == uf.find(j):
                    continue
                if _similar(norm_keys[i], norm_keys[j]) >= config.similarity_threshold:
                    uf.union(i, j)

    # Build clusters
    clusters: Dict[int, List[str]] = {}
    for t in unique_terms:
        root = uf.find(idx[t])
        clusters.setdefault(root, []).append(t)

    # Choose canonical label per cluster:
    # - if manual_map provides one, use it
    # - else choose the "best-looking" member (longest, most letters), then Title Case it
    root_to_canon: Dict[int, str] = {}
    # Build reverse lookup for manual canonical
    manual_canon_set = set(manual_key_to_canon.values())

    for root, members in clusters.items():
        # If any member matches a manual canonical by key, use that manual canonical.
        manual_hit = None
        for m in members:
            mk = _normalize_key(m)
            if mk in manual_key_to_canon:
                manual_hit = manual_key_to_canon[mk]
                break
        if manual_hit is not None:
            root_to_canon[root] = manual_hit
            continue

        # Otherwise pick a representative.
        def score(s: str) -> Tuple[int, int]:
            letters = sum(ch.isalpha() for ch in s)
            return (letters, len(s))

        rep = max(members, key=score)
        # Title-case while preserving roman numerals, but don’t overdo transformations
        root_to_canon[root] = _title_case_preserve_roman(rep)

    # Create term to canonical mapping for quick lookup
    term_to_canon: Dict[str, str] = {}
    for t in unique_terms:
        root = uf.find(idx[t])
        term_to_canon[t] = root_to_canon[root]

    # Write output CSV: all original columns + normalized_name
    with output_csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        
        # Write header with new column
        if has_header and header:
            w.writerow(header + ["normalized_name"])
        
        # Write data rows
        for i, row in enumerate(processing_rows):
            if not row:
                continue
            
            # Get the original name from the specified column
            orig_name = row[name_column_index].strip() if len(row) > name_column_index else ""
            
            # Get normalized name
            if orig_name and orig_name in term_to_canon:
                normalized_name = term_to_canon[orig_name]
            else:
                normalized_name = orig_name  # Keep original if not found or empty
            
            # Write row with normalized name appended
            w.writerow(row + [normalized_name])


# Example usage:
if __name__ == "__main__":
    manual = {
        "EQ2": "EverQuest II",
        "EQII": "EverQuest II", 
        "EverQuest 2": "EverQuest II",
        "eq 2": "EverQuest II",
        "everquest": "EverQuest",
        "everquest 2": "EverQuest II",
        "ff3": "Final Fantasy III",
        "ffxiv": "Final Fantasy XIV",
        "dc universe online": "DC Universe Online",
        "eve online": "EVE Online",
        # Add more common gaming abbreviations
        "CRPG": "CRPG",
        "city of heroes": "City of Heroes",
    }

    write_normalized_csv(
        "categories.csv",
        "categories_normalized.csv",
        manual_map=manual,
        config=NormalizerConfig(similarity_threshold=1.0, min_len_for_fuzzy=100),  # Effectively disable fuzzy matching
        name_column_index=2,  # The 'name' column is at index 2 (0-indexed)
        has_header=True,      # Our CSV has a header row
    )
    print("Wrote categories_normalized.csv")
