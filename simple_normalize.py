import csv
from pathlib import Path
from typing import Dict, Optional
import re
import html

def decode_entities_and_normalize_quotes(text: str) -> str:
    """Decode HTML entities and normalize quotes/dashes."""
    if not text:
        return text
    
    # Decode HTML entities first
    text = html.unescape(text)
    
    # Replace fancy quotes with ASCII equivalents (using unicode escapes)
    text = re.sub(r'[\u2018\u2019]', "'", text)  # Smart single quotes
    text = re.sub(r'[\u201C\u201D]', '"', text)  # Smart double quotes
    
    # Replace en-dashes and em-dashes with hyphens
    text = re.sub(r'[\u2013\u2014]', '-', text)
    
    return text

def proper_title_case(text: str) -> str:
    """Apply proper title case with articles/prepositions in lowercase."""
    if not text:
        return text
    
    # First decode entities and normalize quotes/dashes
    text = decode_entities_and_normalize_quotes(text)
    
    # Words that should be lowercase unless they're first or last
    articles = {'a', 'an', 'the', 'and', 'or', 'but', 'nor', 'for', 'yet', 'so', 
               'at', 'by', 'in', 'of', 'on', 'to', 'up', 'as', 'it', 'is', 'with'}
    
    # Special cases that should maintain their capitalization
    special_cases = {
        'mmo': 'MMORPG',
        'mmos': 'MMORPG', 
        'mmorpg': 'MMORPG',
        'openai': 'OpenAI',
        'amd': 'AMD',
        'nvidia': 'NVIDIA',
        'ps2': 'PS2',
        'ps3': 'PS3', 
        'ps4': 'PS4',
        'ps5': 'PS5',
        'psvr2': 'PSVR2',
        'pcsx2': 'PCSX2',
        'psx': 'PSX',
        'xbox': 'Xbox',
        'nintendo': 'Nintendo',
        'pc': 'PC',
        'vr': 'VR',
        'ar': 'AR',
        'ai': 'AI',
        'ui': 'UI',
        'ux': 'UX',
        'api': 'API',
        'sdk': 'SDK',
        'ide': 'IDE',
        'sql': 'SQL',
        'html': 'HTML',
        'css': 'CSS',
        'ios': 'iOS',
        'macos': 'macOS',
        'linux': 'Linux',
        'windows': 'Windows',
        'rpg': 'RPG',
        'rts': 'RTS',
        'fps': 'FPS',
        'moba': 'MOBA',
        'crpg': 'CRPG',
        '7srl': '7DRL',  # typo fix
        'tis-100': 'TIS-100',
        'cities xl': 'Cities XL',
        'boc': 'Blue Oyster Cult',
        'captaincon': 'CaptainCon',
        'pico8': 'Pico-8',
        'plain white t\'s': 'Plain White Tees',
        'sf': 'Sci Fi',
        'sci-fi': 'Sci Fi',
        'scifi': 'Sci Fi',
        'science fiction': 'Sci Fi',
        'aim': 'Adventures in Monopoly',
        'cpu': 'CPU',
        'gpu': 'GPU',
        'ram': 'RAM',
        'ssd': 'SSD',
        'hdd': 'HDD',
        'usb': 'USB',
        'wifi': 'WiFi',
        'bluetooth': 'Bluetooth',
        'http': 'HTTP',
        'https': 'HTTPS',
        'url': 'URL',
        'json': 'JSON',
        'xml': 'XML',
        'pdf': 'PDF',
        'gif': 'GIF',
        'png': 'PNG',
        'jpg': 'JPG',
        'jpeg': 'JPEG'
    }
    
    # Check if the entire text (lowercase) is a special case
    text_lower = text.lower().strip()
    if text_lower in special_cases:
        return special_cases[text_lower]
    
    # Handle hyphenated terms and preserve existing structure
    words = re.split(r'(\s+|[-:])', text)
    result_words = []
    
    for i, word in enumerate(words):
        if not word or word.isspace() or word in ['-', ':']:
            result_words.append(word)
            continue
            
        word_lower = word.lower()
        
        # Check for special cases first
        if word_lower in special_cases:
            result_words.append(special_cases[word_lower])
            continue
            
        # Skip non-alphabetic tokens (already processed above)
        if not any(c.isalpha() for c in word):
            result_words.append(word)
            continue
            
        # Apply title case rules
        if word_lower in articles and i > 0 and i < len(words) - 1:
            # Keep articles lowercase unless they're first or last word
            # But skip if previous/next word is punctuation
            prev_word_idx = i - 1
            next_word_idx = i + 1
            while prev_word_idx >= 0 and not any(c.isalpha() for c in words[prev_word_idx]):
                prev_word_idx -= 1
            while next_word_idx < len(words) and not any(c.isalpha() for c in words[next_word_idx]):
                next_word_idx += 1
                
            if prev_word_idx >= 0 and next_word_idx < len(words):
                result_words.append(word_lower)
            else:
                result_words.append(word.capitalize())
        else:
            # Regular title case
            result_words.append(word.capitalize())
    
    result = ''.join(result_words)
    
    # Handle dimensionality AFTER title case processing: 2d -> 2D, 3d -> 3D
    result = re.sub(r'\b2d\b', '2D', result, flags=re.IGNORECASE)
    result = re.sub(r'\b3d\b', '3D', result, flags=re.IGNORECASE)
    
    return result

def simple_normalize(text: str) -> str:
    """Simple normalization: proper title case with special handling."""
    if not text:
        return text
        
    # Basic cleanup and entity decoding
    text = decode_entities_and_normalize_quotes(text.strip())
    
    # Handle common game abbreviations and fixes first
    text_lower = text.lower().strip()
    
    # Direct mappings that override everything else
    direct_mappings = {
        'mmo': 'MMORPG',
        'mmos': 'MMORPG',
        'mmorpg': 'MMORPG',
        'openai': 'OpenAI',
        '7srl': '7DRL',  # typo fix
        'tis-100': 'TIS-100',
        'ps2': 'PS2',
        'ps3': 'PS3',
        'ps4': 'PS4', 
        'ps5': 'PS5',
        'psvr2': 'PSVR2',
        'pcsx2': 'PCSX2', 
        'psx': 'PSX',
        'crpg': 'CRPG',
        'cities xl': 'Cities XL',
        'boc': 'Blue Oyster Cult',
        'captaincon': 'CaptainCon',
        'pico8': 'Pico-8',
        'plain white t\'s': 'Plain White Tees',
        'plain white ts': 'Plain White Tees',
        'sf': 'Sci Fi',
        'sci-fi': 'Sci Fi',
        'scifi': 'Sci Fi',
        'science fiction': 'Sci Fi',
        'aim': 'Adventures in Monopoly',
        'soe': 'Sony Online Entertainment',
        'pokemon tcg pocket': 'Pokemon TCG Pocket',
        'sages': 'Sage',
        'scott pilgri': 'Scott Pilgrim',
        'roman numeral number iii': 'Roman Numeral III',
        'stw': 'STW',
        'sw': 'SW',
        't.king': 'T.King',
        'tlp': 'TLP',
        'ups': 'UPS'
    }
    
    if text_lower in direct_mappings:
        return direct_mappings[text_lower]
    
    # Apply proper title case
    return proper_title_case(text)

def simple_normalize_csv(
    input_csv_path: str | Path,
    output_csv_path: str | Path,
    manual_map: Optional[Dict[str, str]] = None,
    name_column_index: int = 2,
    has_header: bool = True
) -> None:
    """
    Simple normalization that handles:
    - Proper title case with articles in lowercase
    - Manual mappings
    - Gaming/tech abbreviations 
    - Common typos and variants
    """
    input_csv_path = Path(input_csv_path)
    output_csv_path = Path(output_csv_path)
    manual_map = manual_map or {}
    
    # Normalize manual map keys
    manual_lower = {k.lower().strip(): v for k, v in manual_map.items()}
    
    rows = []
    with input_csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        if has_header:
            header = next(reader, None)
            if header:
                rows.append(header)
        
        for row in reader:
            if not row:
                continue
            rows.append(row)
    
    # Process rows (skip header if present)
    processing_rows = rows[1:] if has_header else rows
    
    with output_csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        
        # Write header with new column
        if has_header and rows:
            w.writerow(rows[0] + ["normalized_name"])
        
        # Process data rows
        for row in processing_rows:
            if not row:
                continue
            
            # Get original name
            orig_name = row[name_column_index].strip() if len(row) > name_column_index else ""
            
            # Check manual mappings first
            if orig_name.lower().strip() in manual_lower:
                normalized_name = manual_lower[orig_name.lower().strip()]
            else:
                normalized_name = simple_normalize(orig_name)
            
            # Write row with normalized name
            w.writerow(row + [normalized_name])

if __name__ == "__main__":
    manual_mappings = {
        # Game abbreviations and variants
        "EQ": "EverQuest",
        "EQ2": "EverQuest II",
        "EQII": "EverQuest II", 
        "EverQuest 2": "EverQuest II",
        "everquest": "EverQuest",
        "everquest 2": "EverQuest II",
        "eq 2": "EverQuest II",
        
        # Final Fantasy variants
        "FF1": "Final Fantasy",
        "ff1": "Final Fantasy",
        "FF3": "Final Fantasy III",
        "FFXIV": "Final Fantasy XIV", 
        "FF14": "Final Fantasy XIV",
        "ff3": "Final Fantasy III",
        "ffxiv": "Final Fantasy XIV",
        "ff14": "Final Fantasy XIV",
        "Final Fantasy III": "Final Fantasy III",
        "final fantasy iii": "Final Fantasy III",
        "Final Fantasy VI": "Final Fantasy VI",
        "final fantasy vi": "Final Fantasy VI",
        "Final Fantasy VII": "Final Fantasy VII", 
        "final fantasy vii": "Final Fantasy VII",
        "Final Fantasy XI": "Final Fantasy XI",
        "final fantasy xi": "Final Fantasy XI",
        "Final Fantasy XII": "Final Fantasy XII",
        "final fantasy xii": "Final Fantasy XII",
        "Final Fantasy XIII": "Final Fantasy XIII",
        "final fantasy xiii": "Final Fantasy XIII",
        "Final Fantasy XIV": "Final Fantasy XIV",
        "final fantasy xiv": "Final Fantasy XIV",
        "Final Fantasy XVI": "Final Fantasy XVI",
        "final fantasy xvi": "Final Fantasy XVI",
        
        # Other games
        "DC Universe Online": "DC Universe Online",
        "dc universe online": "DC Universe Online",
        "dcuo": "DC Universe Online",
        "DCUO": "DC Universe Online", 
        "EVE Online": "EVE Online",
        "eve online": "EVE Online",
        "City of Heroes": "City of Heroes",
        "city of heroes": "City of Heroes",
        "ghosts of tsushima": "Ghost of Tsushima",
        "Ghosts of Tsushima": "Ghost of Tsushima",
        "nethack": "NetHack",
        "NetHack": "NetHack",
        
        # Common duplicates and case variants
        "comic": "Comic",
        "comics": "Comic",
        "Comic": "Comic",
        "Comics": "Comic",
        
        "blockchain": "Blockchain",
        "Blockchain": "Blockchain",
        
        # MMO variants (all map to MMORPG)
        "MMO": "MMORPG",
        "mmo": "MMORPG", 
        "MMOs": "MMORPG",
        "mmos": "MMORPG",
        "MMORPG": "MMORPG",
        "mmorpg": "MMORPG",
        
        # Tech companies and terms
        "OpenAI": "OpenAI",
        "openai": "OpenAI",
        "soe": "Sony Online Entertainment",
        "SOE": "Sony Online Entertainment",
        
        # Gaming platforms and hardware
        "PS2": "PS2",
        "ps2": "PS2", 
        "playstation 2": "PS2",
        "Playstation 2": "PS2",
        "PS3": "PS3",
        "ps3": "PS3",
        "playstation 3": "PS3",
        "Playstation 3": "PS3",
        "PS4": "PS4", 
        "ps4": "PS4",
        "PS5": "PS5",
        "ps5": "PS5",
        "PSVR2": "PSVR2",
        "psvr2": "PSVR2",
        "PCSX2": "PCSX2",
        "pcsx2": "PCSX2",
        "PSX": "PSX",
        "psx": "PSX",
        "playstation": "PSX",
        "Playstation": "PSX",
        "nes": "NES",
        "NES": "NES",
        "nintendo ds": "Nintendo DS",
        "Nintendo DS": "Nintendo DS",
        
        # Game-specific terms
        "pokemon tcg pocket": "Pokemon TCG Pocket",
        "Pokemon TCG Pocket": "Pokemon TCG Pocket",
        "progressquest": "ProgressQuest",
        "ProgressQuest": "ProgressQuest",
        "roguelike": "Rogue-Like",
        "Roguelike": "Rogue-Like",
        "Rogue-like": "Rogue-Like",
        "rogue-like": "Rogue-Like",
        "scott pilgri": "Scott Pilgrim",
        "Scott Pilgri": "Scott Pilgrim",

        # Specific games and terms
        "Cities XL": "Cities XL",
        "cities xl": "Cities XL",
        "Boc": "Blue Oyster Cult",
        "boc": "Blue Oyster Cult",
        "CaptainCon": "CaptainCon", 
        "captaincon": "CaptainCon",
        "Pico-8": "Pico-8",
        "pico8": "Pico-8",
        "Plain White Tees": "Plain White Tees",
        "plain white t's": "Plain White Tees",
        "plain white ts": "Plain White Tees",
        
        # Science Fiction variants
        "SF": "Sci Fi",
        "sf": "Sci Fi",
        "Sci-Fi": "Sci Fi",
        "sci-fi": "Sci Fi",
        "SciFi": "Sci Fi",
        "scifi": "Sci Fi",
        "Science Fiction": "Sci Fi",
        "science fiction": "Sci Fi",
        
        # Game/Category specific  
        "AIM": "Adventures in Monopoly",
        "aim": "Adventures in Monopoly",
        
        # Preserve specific capitalizations
        "DC Comics": "DC Comics",
        "dc comics": "DC Comics", 
        "DOS Games": "DOS Games",
        "dos games": "DOS Games",
        "NFT": "NFT",
        "nft": "NFT",
        "THE400 Mini": "THE400 Mini",
        "the400 mini": "THE400 Mini",
        
        # World of Warcraft variants
        "WoW": "WoW",
        "wow": "World of Warcraft",
        "Wow": "World of Warcraft", 
        "World of Warcraft": "World of Warcraft",
        "world of warcraft": "World of Warcraft",
        "wow-like": "WoW-Like",
        "WoW-like": "WoW-Like",
        "WoW-Like": "WoW-Like",
        "wow like": "WoW-Like",
        "WoW like": "WoW-Like",
        
        # Acronyms that should be uppercase
        "STW": "STW",
        "stw": "STW",
        "SW": "SW", 
        "sw": "SW",
        "TLP": "TLP",
        "tlp": "TLP",
        "FTL": "FTL",
        "ftl": "FTL",
        "dcc": "Dungeon Crawl Classic",
        "DCC": "Dungeon Crawl Classic",
        "f2p": "F2P",
        "F2P": "F2P",
        "ltt": "LTT",
        "LTT": "LTT",
        "gti": "GTI",
        "GTI": "GTI",
        "tdd": "Test Driven Development",
        "TDD": "Test Driven Development",
        "ttrpg": "TTRPG",
        "TTRPG": "TTRPG",
        "zpg": "ZPG",
        "ZPG": "ZPG",
        "UPS": "UPS",
        "ups": "UPS",
        
        # Names and proper nouns
        "T.King": "T.King",
        "t.king": "T.King",
        "king louis xvi": "King Louis XVI",
        "King Louis Xvi": "King Louis XVI",
        "dc superheroes united": "DC Superheroes United",
        "Dc Superheroes United": "DC Superheroes United",
        "lillput workshop": "Lilliput Workshop",
        "Lillput Workshop": "Lilliput Workshop",
        "hoard's llc": "Hoard's LLC",
        "Hoard's Llc": "Hoard's LLC",
        "free as in speach": "Free as in Speech",
        "Free as in Speach": "Free as in Speech",
        "iPhone": "iPhone",
        "iphone": "iPhone",
        "GIMP": "GIMP",
        "gimp": "GIMP",
        "roman numeral number iii": "Roman Numeral III",
        "Roman Numeral Number III": "Roman Numeral III",
        "Roman Numeral Number Iii": "Roman Numeral III",
        "sages": "Sage",
        "Sages": "Sage",
        "team spod": "Team Spode",
        "Team Spod": "Team Spode",
        "uss monterey": "USS Monterey",
        "Uss Monterey": "USS Monterey",
        "videogame": "Video Game",
        "Videogame": "Video Game",
        "warslick woods": "Warsliks Woods",
        "Warslick Woods": "Warsliks Woods",
        "warslik woods": "Warsliks Woods",
        "Warslik Woods": "Warsliks Woods",
        "webring": "Web Ring",
        "Webring": "Web Ring",
        "wizard 101": "Wizard101",
        "Wizard 101": "Wizard101",
        
        # Typo fixes
        "7SRL": "7DRL",
        "7srl": "7DRL",
        
        # Preserve specific formatting
        "TIS-100": "TIS-100",
        "tis-100": "TIS-100",
        
        # RPG variants
        "CRPG": "CRPG",
        "crpg": "CRPG",
        
        # Strategy game genres
        "4x": "4X",
        "4X": "4X",
        
        # Dimensionality fixes
        "2d": "2D",
        "3d": "3D",
        "2D": "2D", 
        "3D": "3D",
        
        # D&D variants should be normalized
        "d&d": "D&D",
        "D&D": "D&D",
    }
    
    simple_normalize_csv(
        "categories.csv",
        "categories_simple_normalized.csv",
        manual_map=manual_mappings,
        name_column_index=2,
        has_header=True
    )
    print("Wrote categories_simple_normalized.csv with comprehensive normalization")