# Shared Python/Go Neva language data

Neva remains the **sole authoritative language repository**. The 17-column
`data/neva_dictionary_v1_1.csv` contains every word and its provenance.
The separate, versioned `data/translation_lexicon.json` contains hand-curated
English semantic inventories not safely inferable from raw dictionary glosses:

- `english_nouns`: supported English noun meaning → canonical Neva headword.
- `verbs`: Neva infinitive → English base, third-singular, past, participle.
- `english_adjectives`, `prepositions`, `mass_nouns`: restricted
  translation grammar semantics, **not** automatic coverage of all entries.
- `strong_past`: approved closed class of exceptional Neva past stems.
- `phrases`: accepted bidirectional conversational phrases and punctuation.

`scripts/neva_data.py` loads the JSON using Python's standard library.
`scripts/neva.py`, `scripts/neva_translate.py` and `scripts/neva_phrases.py`
consume the shared definitions rather than independently maintaining their lists.

ChapterGuides' Go runtime checks out this public repository without credentials
on startup and at a configurable interval. It parses the CSV and JSON from one
checkout and validates the *entire candidate* before replacing the in-memory
dictionary. SHA-256 changes indicate a **candidate update**, not its validity.
If Git is offline or the candidate is invalid, the running service retains its
last-known-good snapshot. A checked-in Neva fallback remains available.

To extend supported translator vocabulary, make the change **here** alongside
the canonical CSV; do not edit the Git clone under ChapterGuides' `tmp/` or fork
these curated tables in Go. For new or changed rules, coordinate tested updates
across Python and Go: the JSON is language data, not a portable Python parser.
