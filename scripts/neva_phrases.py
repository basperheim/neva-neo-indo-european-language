"""Small bilingual phrasebook for Neva greetings and routine utterances.

All phrases are explicit Neva coinages or forms from the existing lexicon.
No automatic language identification, model inference, or PIE authenticity claim.
"""
from __future__ import annotations

import re

# The Python translator and ChapterGuides Go consume the same authored list.
from neva_data import lexical_data

_PHRASE_DATA = lexical_data()["phrases"]
_PHRASES = dict(_PHRASE_DATA["en_to_neva"])
_NEVA_TO_ENGLISH = dict(_PHRASE_DATA["neva_to_en"])
_CANONICAL_PUNCTUATION = dict(_PHRASE_DATA["canonical_punctuation"])


def translate_phrase(text: str, source: str, target: str) -> str | None:
    """Translate a known phrase; ignore surrounding whitespace/final punctuation.

    Returns None if not a recognized phrase. Does not interpret arbitrary text
    or distinguish homonymous phrases in a larger grammatical context.
    """
    stripped = text.strip()
    match = re.fullmatch(r"([A-Za-z]+(?:\s+[A-Za-z]+)*)\s*([.!?])?", stripped)
    if not match:
        return None

    normalized = " ".join(match.group(1).casefold().split())
    punct = match.group(2)
    if source == "en" and target == "neva":
        converted = _PHRASES.get(normalized)
    elif source == "neva" and target == "en":
        converted = _NEVA_TO_ENGLISH.get(normalized)
    else:
        return None
    if converted is None:
        return None
    if not punct:
        punct = _CANONICAL_PUNCTUATION.get(normalized, "")
    return converted[0].upper() + converted[1:] + punct
