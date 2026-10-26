"""A bounded two-clause Neva ↔ English translator.

This is not a free-form natural-language parser. It composes the validated
simple-clause translator, accepts only one conditional/causal relation,
or one simple postnominal relative clause, and explicitly rejects nesting.
"""
from __future__ import annotations

import re

from neva_relatives import is_relative, matching_cases

# No automatic "ja" feminine relative; it already means "yes".
_RELATIVE_HEADWORDS = {"M": "jos", "F": "josa", "N": "jod"}
_PRONOUNS = {"M": "So", "F": "Sa", "N": "Tod"}
_HUMAN_NOUNS = {
    "mother", "father", "brother", "sister", "daughter", "son",
    "child", "human being", "man", "woman",
}


def _body(text: str) -> tuple[str, str]:
    match = re.fullmatch(r"\s*([A-Za-z][A-Za-z\s,]*?)\s*([.!?]?)\s*", text)
    if not match:
        raise ValueError("only one or two short clauses with an optional comma are supported")
    return match.group(1).strip(), match.group(2) or "."


def _base_translate(piece: str, source: str) -> str:
    # Import lazily to avoid a circular import with neva_translate.translate().
    from neva_translate import from_english, from_neva
    value = (from_neva if source == "neva" else from_english)(piece.strip() + ".")
    return value.rstrip(".")


def _lower_start(s: str) -> str:
    # English first-person 'I' is always uppercase, including after a comma.
    if s == "I" or s.startswith("I "):
        return s
    return s[0].lower() + s[1:] if s else s


def _upper_start(s: str) -> str:
    return s[0].upper() + s[1:] if s else s


def _no_nested_conjunctions(piece: str) -> None:
    if re.search(r"\b(jaba|kod|if|because)\b", piece, flags=re.I):
        raise ValueError("nested conditional and causal clauses are not supported")


def _two_clauses(text: str, source: str) -> str | None:
    body, punct = _body(text)
    if punct == "?":
        return None
    if source == "neva":
        m = re.fullmatch(r"jaba\s+([^,]+),\s*(.+)", body, flags=re.I)
        if m:
            a, b = m.groups()
            _no_nested_conjunctions(a)
            _no_nested_conjunctions(b)
            return f"If {_lower_start(_base_translate(a, source))}, {_lower_start(_base_translate(b, source))}{punct}"
        m = re.fullmatch(r"kod\s+([^,]+),\s*(.+)", body, flags=re.I)
        if m:
            a, b = m.groups()
            _no_nested_conjunctions(a)
            _no_nested_conjunctions(b)
            return f"Because {_lower_start(_base_translate(a, source))}, {_lower_start(_base_translate(b, source))}{punct}"
        for word, english in (("jaba", "if"), ("kod", "because")):
            m = re.fullmatch(rf"(.+?)\s+{word}\s+(.+)", body, flags=re.I)
            if m:
                a, b = m.groups()
                _no_nested_conjunctions(a)
                _no_nested_conjunctions(b)
                return (_upper_start(_base_translate(a, source)) +
                        " " + english + " " + _lower_start(_base_translate(b, source)) + punct)
        if re.search(r"\b(jaba|kod)\b", body, flags=re.I):
            raise ValueError("use 'Jaba <condition>, <result>' or '<result> kod <cause>'")
        match = re.fullmatch(r"(.+?)\s+(ke|ve|at)\s+(.+)", body, flags=re.I)
        if match:
            first, conjunction, second = match.groups()
            try:
                left = _base_translate(first, source)
                right = _base_translate(second, source)
            except ValueError:
                return None  # e.g. 'pen ke computer' is object coordination
            word = {"ke": "and", "ve": "or", "at": "but"}[conjunction.lower()]
            return _upper_start(left) + " " + word + " " + _lower_start(right) + punct
        return None
    else:
        m = re.fullmatch(r"if\s+([^,]+),\s*(.+)", body, flags=re.I)
        if m:
            a, b = m.groups()
            _no_nested_conjunctions(a)
            _no_nested_conjunctions(b)
            return ("Jaba " + _lower_start(_base_translate(a, source)) +
                    ", " + _lower_start(_base_translate(b, source)) + punct)
        m = re.fullmatch(r"because\s+([^,]+),\s*(.+)", body, flags=re.I)
        if m:
            a, b = m.groups()
            _no_nested_conjunctions(a)
            _no_nested_conjunctions(b)
            return ("Kod " + _lower_start(_base_translate(a, source)) +
                    ", " + _lower_start(_base_translate(b, source)) + punct)
        for word, neva in (("if", "jaba"), ("because", "kod")):
            m = re.fullmatch(rf"(.+?)\s+{word}\s+(.+)", body, flags=re.I)
            if m:
                a, b = m.groups()
                _no_nested_conjunctions(a)
                _no_nested_conjunctions(b)
                return (_upper_start(_base_translate(a, source)) + " " + neva +
                        " " + _lower_start(_base_translate(b, source)) + punct)
        if re.search(r"\b(if|because)\b", body, flags=re.I):
            raise ValueError("use 'If <condition>, <result>' or '<result> because <cause>'")
        match = re.fullmatch(r"(.+?)\s+(and|or|but)\s+(.+)", body, flags=re.I)
        if match:
            first, conjunction, second = match.groups()
            try:
                left = _base_translate(first, source)
                right = _base_translate(second, source)
            except ValueError:
                return None  # one noun phrase may contain 'and'
            word = {"and": "ke", "or": "ve", "but": "at"}[conjunction.lower()]
            return _upper_start(left) + " " + word + " " + _lower_start(right) + punct
        return None


def _relative_from_neva(text: str) -> str | None:
    import neva_translate as t
    body, punct = _body(text)
    words = body.lower().split()
    positions = [idx for idx, word in enumerate(words) if is_relative(word)]
    if not positions:
        return None
    if len(positions) != 1 or "," in body:
        raise ValueError("only one postnominal relative clause is supported")
    index = positions[0]
    prefix, relative, tail = words[:index], words[index], words[index + 1:]
    if len(prefix) < 2 or not tail or not prefix[-1] in t.noun_forms():
        raise ValueError("a relative clause must follow its antecedent noun after a main verb")
    if not any(word in t.finite_forms() for word in prefix):
        raise ValueError("a relative clause must follow a complete main clause")
    antecedents = [
        n for n in t.noun_forms()[prefix[-1]]
        if matching_cases(relative, n.gender, n.number)
    ]
    if len({(n.word, n.gender, n.number) for n in antecedents}) != 1:
        raise ValueError("relative antecedent is ambiguous; use a clearer noun phrase")
    noun = antecedents[0]
    cases = matching_cases(relative, noun.gender, noun.number)
    main = _base_translate(" ".join(prefix), "neva")
    if "nominative" in cases and any(
        (item[1] == (2 if noun.number == "singular" else 5))
        for word in tail for item in t.finite_forms().get(word, [])
    ):
        subject = (_PRONOUNS[noun.gender] if noun.number == "singular" else "Toi")
        sub = _base_translate(subject + " " + " ".join(tail), "neva")
        lead = {"M": "He", "F": "She", "N": "It"}[noun.gender] if noun.number == "singular" else "They"
        if not sub.startswith(lead + " "):
            raise ValueError("relative clause subject could not be resolved")
        clause = sub[len(lead) + 1:]
    elif "accusative" in cases:
        # Restrict missing-object relatives to a short finite verb phrase.
        if len(tail) > 3 or not any(word in t.finite_forms() for word in tail):
            raise ValueError("only short relative-object clauses are supported")
        clause = _lower_start(_base_translate(" ".join(tail), "neva"))
    else:
        raise ValueError("genitive/dative relative syntax is not supported yet")
    marker = "who" if noun.english in _HUMAN_NOUNS else "that"
    return _upper_start(main) + " " + marker + " " + _lower_start(clause) + punct


def _relative_from_english(text: str) -> str | None:
    import neva
    import neva_translate as t
    body, punct = _body(text)
    m = re.fullmatch(r"(.+?)\s+(who|that)\s+([a-z][a-z ]+)", body, flags=re.I)
    if not m or "," in body:
        return None
    main, connector, tail = m.groups()
    noun_gloss = main.lower().split()[-1]
    neva_noun = t.ENGLISH_NOUNS.get(noun_gloss)
    if neva_noun is None:
        # "I see that mother" uses a demonstrative determiner, not a
        # relative pronoun. Let the ordinary simple-clause parser handle it.
        return None
    entry = next(x for x in neva.load_lexicon() if x["Neva"] == neva_noun)
    gender = entry["Gender"]
    if connector.lower() == "who" and noun_gloss not in _HUMAN_NOUNS:
        raise ValueError("use 'that' for this nonhuman antecedent")
    main_neva = _base_translate(main, "en")
    lead = {"M": "he", "F": "she", "N": "it"}[gender]
    subordinate = _base_translate(lead + " " + tail, "en")
    # Full grammatical subject is supplied by the relative pronoun instead.
    first, _, remainder = subordinate.partition(" ")
    if first.casefold() != {"M": "so", "F": "sa", "N": "tod"}[gender] or not remainder:
        raise ValueError("could not resolve subject of relative clause")
    return _upper_start(main_neva) + " " + _RELATIVE_HEADWORDS[gender] + " " + remainder + punct


def translate_complex(text: str, source: str, target: str) -> str | None:
    """Return a limited translation, None if no supported complex syntax found.

    Errors use TranslationError to retain the caller's strict/passthrough policy.
    """
    from neva_translate import TranslationError
    try:
        if source == "neva" and target == "en":
            result = _two_clauses(text, source) or _relative_from_neva(text)
        elif source == "en" and target == "neva":
            result = _two_clauses(text, source) or _relative_from_english(text)
        else:
            return None
    except ValueError as exc:
        raise TranslationError(str(exc)) from exc
    return result
