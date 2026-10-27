"""Shared, versioned Neva lexical/translation data for Python and Go.

The original repository owns this JSON, including curated semantic choices.
Keep the canonical 17-column CSV as the dictionary source of truth.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

LEXICAL_DATA = Path(__file__).resolve().parents[1] / "data" / "translation_lexicon.json"


@lru_cache(maxsize=1)
def lexical_data() -> dict:
    with LEXICAL_DATA.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported Neva shared lexical data schema")
    required = ("english_nouns", "verbs", "english_adjectives",
                "prepositions", "mass_nouns", "strong_past", "phrases")
    if any(key not in data for key in required):
        raise ValueError("Incomplete Neva shared lexical data")
    return data
