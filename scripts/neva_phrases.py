"""Small bilingual phrasebook for Neva greetings and routine utterances.

All phrases are explicit Neva coinages or forms from the existing lexicon.
No automatic language identification, model inference, or PIE authenticity claim.
"""
from __future__ import annotations

import re

# English --> Neva. The forms are provisional conversational conventions.
# vese "well" is reused as a greeting; vesom agrees with neuter deinom "day".
_PHRASES = {
    "hello": "vese",
    "hi": "vese",
    "good day": "vesom deinom",
    "how are you": "komo es",
    "i am well": "em vese",
}

_NEVA_TO_ENGLISH = {
    "vese": "Hello",
    "vesom deinom": "Good day",
    "komo es": "How are you",
    "em vese": "I am well",
}

_CANONICAL_PUNCTUATION = {
    "how are you": "?",
    "komo es": "?",
}


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
