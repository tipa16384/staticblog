#!/usr/bin/env python3
"""Populate static relatedPosts front matter for Hugo content.

This script reads categories/tags from post front matter, finds the closest posts,
and writes a static `relatedPosts` list into front matter.

Usage examples:
  python scripts/populate_related_posts.py --target content/posts/2026/03/25/everquest-3-is-officially-dead.md
  python scripts/populate_related_posts.py --all
  python scripts/populate_related_posts.py --all --dry-run
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z0-9_]+):")
LIST_ITEM_RE = re.compile(r"^\s*-\s*(.+?)\s*$")


@dataclass
class Post:
    file_path: Path
    permalink: str
    title: str
    thumbnail_image: str
    frontmatter_lines: list[str]
    body_lines: list[str]
    newline: str
    tags_display: list[str]
    categories_display: list[str]
    tags_norm: set[str]
    categories_norm: set[str]
    date: dt.datetime
    draft: bool


def detect_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def split_frontmatter(text: str) -> tuple[list[str], list[str]]:
    normalized = text.replace("\r\n", "\n")
    lines = normalized.split("\n")

    if not lines or lines[0].strip() != "---":
        raise ValueError("File does not start with YAML front matter delimiter")

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        raise ValueError("Could not find closing YAML front matter delimiter")

    fm_lines = lines[1:end_idx]
    body_lines = lines[end_idx + 1 :]
    return fm_lines, body_lines


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2:
        if value[0] == '"' and value[-1] == '"':
            inner = value[1:-1]
            # Process YAML double-quoted escape sequences (\" → ", \\ → \, etc.)
            inner = re.sub(r'\\(.)', lambda m: m.group(1) if m.group(1) in '"\\ntr' else '\\' + m.group(1), inner)
            # Strip any residual backslash-before-doublequote from doubled escaping in prior runs
            inner = re.sub(r'\\+"', '"', inner)
            return inner
        if value[0] == "'" and value[-1] == "'":
            inner = value[1:-1]
            # Single-quoted YAML has no backslash escapes; clean up bad legacy \" artifacts
            inner = re.sub(r'\\+"', '"', inner)
            return inner.replace("''", "'")
    return value


def parse_scalar(frontmatter_lines: list[str], key: str) -> str | None:
    prefix = f"{key}:"
    for line in frontmatter_lines:
        if line.startswith(prefix):
            return unquote(line[len(prefix) :].strip())
    return None


def find_key_block(lines: list[str], key: str) -> tuple[int, int] | None:
    prefix = f"{key}:"
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            j = i + 1
            while j < len(lines):
                if lines[j].startswith("  ") or lines[j].startswith("\t") or lines[j].strip() == "":
                    j += 1
                    continue
                break
            return i, j
    return None


def parse_list(frontmatter_lines: list[str], key: str) -> list[str]:
    block = find_key_block(frontmatter_lines, key)
    if not block:
        return []

    start, end = block
    values: list[str] = []
    for line in frontmatter_lines[start + 1 : end]:
        m = LIST_ITEM_RE.match(line)
        if not m:
            continue
        values.append(unquote(m.group(1)))
    return values


def normalize_term(term: str) -> str:
    return term.strip().casefold()


def parse_date(date_value: str | None) -> dt.datetime:
    if not date_value:
        return dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)

    raw = date_value.strip().replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(raw)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=dt.timezone.utc)
        return parsed
    except ValueError:
        return dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)


def parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"true", "yes", "1"}


def build_permalink(file_path: Path, content_root: Path) -> str:
    # Build links relative to the post content root so they start with year/month/day.
    relative = file_path.relative_to(content_root).with_suffix("")
    return "/" + relative.as_posix().strip("/") + "/"


def load_post(file_path: Path, content_root: Path) -> Post | None:
    text = file_path.read_text(encoding="utf-8")
    newline = detect_newline(text)

    try:
        fm_lines, body_lines = split_frontmatter(text)
    except ValueError:
        return None

    tags = parse_list(fm_lines, "tags")
    categories = parse_list(fm_lines, "categories")
    date_value = parse_scalar(fm_lines, "date")
    draft_value = parse_scalar(fm_lines, "draft")
    title = parse_scalar(fm_lines, "title") or file_path.stem
    thumbnail_image = parse_scalar(fm_lines, "thumbnailImage") or parse_scalar(fm_lines, "coverImage") or ""

    return Post(
        file_path=file_path,
        permalink=build_permalink(file_path, content_root),
        title=title,
        thumbnail_image=thumbnail_image,
        frontmatter_lines=fm_lines,
        body_lines=body_lines,
        newline=newline,
        tags_display=tags,
        categories_display=categories,
        tags_norm={normalize_term(t) for t in tags if t.strip()},
        categories_norm={normalize_term(c) for c in categories if c.strip()},
        date=parse_date(date_value),
        draft=parse_bool(draft_value, default=False),
    )


def collect_posts(content_root: Path) -> list[Post]:
    posts: list[Post] = []
    for file_path in sorted(content_root.rglob("*.md")):
        post = load_post(file_path, content_root)
        if post is not None:
            posts.append(post)
    return posts


def build_df(posts: Iterable[Post]) -> tuple[Counter, Counter]:
    tag_df: Counter = Counter()
    category_df: Counter = Counter()

    for post in posts:
        for t in post.tags_norm:
            tag_df[t] += 1
        for c in post.categories_norm:
            category_df[c] += 1

    return tag_df, category_df


def idf_weight(df_value: int, total_docs: int) -> float:
    # Smooth IDF so rare terms score higher than broad/common terms.
    return math.log((total_docs + 1) / (df_value + 1)) + 1.0


def build_inverted_index(posts: list[Post]) -> tuple[dict[str, set[int]], dict[str, set[int]]]:
    tag_index: dict[str, set[int]] = defaultdict(set)
    category_index: dict[str, set[int]] = defaultdict(set)

    for idx, post in enumerate(posts):
        for t in post.tags_norm:
            tag_index[t].add(idx)
        for c in post.categories_norm:
            category_index[c].add(idx)

    return tag_index, category_index


def score_candidate(
    source: Post,
    candidate: Post,
    total_posts: int,
    tag_df: Counter,
    category_df: Counter,
) -> tuple[float, int, int, dt.datetime]:
    common_tags = source.tags_norm & candidate.tags_norm
    common_categories = source.categories_norm & candidate.categories_norm

    tag_overlap = sum(idf_weight(tag_df[t], total_posts) for t in common_tags)
    category_overlap = sum(idf_weight(category_df[c], total_posts) for c in common_categories)

    score = (2.0 * tag_overlap) + (1.0 * category_overlap)
    return score, len(common_tags), len(common_categories), candidate.date


def find_related_for_post(
    source_idx: int,
    posts: list[Post],
    tag_df: Counter,
    category_df: Counter,
    tag_index: dict[str, set[int]],
    category_index: dict[str, set[int]],
    limit: int,
) -> list[Post]:
    source = posts[source_idx]

    candidate_ids: set[int] = set()
    for t in source.tags_norm:
        candidate_ids.update(tag_index.get(t, set()))
    for c in source.categories_norm:
        candidate_ids.update(category_index.get(c, set()))

    candidate_ids.discard(source_idx)

    scored: list[tuple[tuple[float, int, int, dt.datetime], int]] = []
    for idx in candidate_ids:
        candidate = posts[idx]
        if candidate.draft:
            continue

        result = score_candidate(source, candidate, len(posts), tag_df, category_df)
        score_value = result[0]
        if score_value <= 0:
            continue
        scored.append((result, idx))

    scored.sort(
        key=lambda item: (
            item[0][0],  # score
            item[0][1],  # shared tags
            item[0][2],  # shared categories
            item[0][3],  # newer date wins ties
        ),
        reverse=True,
    )

    return [posts[idx] for _, idx in scored[:limit]]


def format_yaml_list(key: str, values: list[str]) -> list[str]:
    escaped_values = [value.replace('"', '\\"') for value in values]
    return [f"{key}:"] + [f'  - "{value}"' for value in escaped_values]


def yaml_quote(value: str) -> str:
    """Quote a YAML scalar, using single quotes if the value contains double quotes."""
    if '"' in value:
        # Escape any single quotes in the value, then wrap in single quotes
        return "'" + value.replace("'", "''") + "'"
    return '"' + value + '"'


def format_related_posts_block(key: str, related_posts: list[Post]) -> list[str]:
    block = [f"{key}:"]
    for post in related_posts:
        url = yaml_quote(post.permalink)
        title = yaml_quote(post.title)
        thumb = yaml_quote(post.thumbnail_image)
        block.extend(
            [
                f'  - url: {url}',
                f'    title: {title}',
                f'    thumbnailImage: {thumb}',
            ]
        )
    return block


def upsert_list_block(lines: list[str], key: str, values: list[str]) -> list[str]:
    out = list(lines)

    existing = find_key_block(out, key)
    if existing:
        start, end = existing
        del out[start:end]

    block = format_yaml_list(key, values)

    tags_block = find_key_block(out, "tags")
    categories_block = find_key_block(out, "categories")

    if tags_block:
        insert_at = tags_block[1]
    elif categories_block:
        insert_at = categories_block[1]
    else:
        insert_at = len(out)

    return out[:insert_at] + block + out[insert_at:]


def render_post(post: Post, updated_frontmatter: list[str]) -> str:
    lines = ["---", *updated_frontmatter, "---", *post.body_lines]
    text = post.newline.join(lines)
    if not text.endswith(post.newline):
        text += post.newline
    return text


def update_post_related(post: Post, related_posts: list[Post], dry_run: bool) -> bool:
    out = list(post.frontmatter_lines)

    existing = find_key_block(out, "relatedPosts")
    if existing:
        start, end = existing
        del out[start:end]

    related_block = format_related_posts_block("relatedPosts", related_posts)

    tags_block = find_key_block(out, "tags")
    categories_block = find_key_block(out, "categories")

    if tags_block:
        insert_at = tags_block[1]
    elif categories_block:
        insert_at = categories_block[1]
    else:
        insert_at = len(out)

    new_fm = out[:insert_at] + related_block + out[insert_at:]

    original_text = render_post(post, post.frontmatter_lines)
    updated_text = render_post(post, new_fm)

    if original_text == updated_text:
        return False

    if not dry_run:
        post.file_path.write_text(updated_text, encoding="utf-8")

    post.frontmatter_lines = new_fm
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Populate static relatedPosts in Hugo front matter")
    parser.add_argument(
        "--content-root",
        default="content/posts",
        help="Root directory containing post markdown files (default: content/posts)",
    )
    parser.add_argument(
        "--target",
        help="Single post file to update (relative to repo root or absolute path)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Update all posts under --content-root",
    )
    parser.add_argument("--limit", type=int, default=4, help="Number of related posts to store (default: 4)")
    parser.add_argument("--dry-run", action="store_true", help="Compute and print changes without writing files")
    parser.add_argument("--verbose", action="store_true", help="Print related matches for each updated post")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.all and not args.target:
        print("Error: provide either --target <file> or --all")
        return 2

    if args.limit < 1:
        print("Error: --limit must be >= 1")
        return 2

    repo_root = Path.cwd()
    content_root = (repo_root / args.content_root).resolve()
    if not content_root.exists():
        print(f"Error: content root does not exist: {content_root}")
        return 2

    posts = collect_posts(content_root)
    if not posts:
        print("No posts found.")
        return 0

    tag_df, category_df = build_df(posts)
    tag_index, category_index = build_inverted_index(posts)

    if args.all:
        target_indexes = list(range(len(posts)))
    else:
        target_path = Path(args.target)
        if not target_path.is_absolute():
            target_path = (repo_root / target_path).resolve()
        else:
            target_path = target_path.resolve()

        post_map = {p.file_path.resolve(): idx for idx, p in enumerate(posts)}
        if target_path not in post_map:
            print(f"Error: target post not found in scanned posts: {target_path}")
            return 2
        target_indexes = [post_map[target_path]]

    changed = 0
    processed = 0

    for idx in target_indexes:
        source = posts[idx]
        if source.draft:
            continue

        related = find_related_for_post(
            source_idx=idx,
            posts=posts,
            tag_df=tag_df,
            category_df=category_df,
            tag_index=tag_index,
            category_index=category_index,
            limit=args.limit,
        )

        did_change = update_post_related(source, related, dry_run=args.dry_run)
        changed += int(did_change)
        processed += 1

        if args.verbose:
            print(f"{source.file_path}:")
            if related:
                for r in related:
                    print(f"  - {r.permalink}")
            else:
                print("  - (no related posts found)")

    mode = "DRY-RUN" if args.dry_run else "WRITE"
    print(f"[{mode}] Processed: {processed} post(s), updated: {changed} post(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
