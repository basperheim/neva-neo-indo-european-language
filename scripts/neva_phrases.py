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
    "yes": "ja",
    "no": "ne",
    "good night": "vesa nokta",
    "where is the door": "ku est dhverom",
    "where is the house": "ku est domom",
    "where is the road": "ku est pontos",
    "go to the door": "ie ad dhverom",
    "go through the door": "ie per dhverom",
    "go to the house": "ie ad domom",
}

_NEVA_TO_ENGLISH = {
    "vese": "Hello",
    "vesom deinom": "Good day",
    "komo es": "How are you",
    "em vese": "I am well",
    "ja": "Yes",
    "ne": "No",
    "vesa nokta": "Good night",
    "ku est dhverom": "Where is the door",
    "ku est domom": "Where is the house",
    "ku est pontos": "Where is the road",
    "ie ad dhverom": "Go to the door",
    "ie per dhverom": "Go through the door",
    "ie ad domom": "Go to the house",
}

_CANONICAL_PUNCTUATION = {
    "how are you": "?",
    "komo es": "?",
    "where is the door": "?",
    "where is the house": "?",
    "where is the road": "?",
    "ku est dhverom": "?",
    "ku est domom": "?",
    "ku est pontos": "?",
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
