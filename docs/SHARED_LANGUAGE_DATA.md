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

## Vocabulary smoke test: `bernos`

The regular masculine noun `bernos` (“boy, young male child”; NEVA-0852)
was added as a Neva adaptation of the Indo-European `*bʰer-` / `*bʰor-no-m`
family, with an explicitly **analogical e-grade** aligned to Neva `beren`.
This is not a claim that `bernos` itself is an attested PIE reconstruction.
Its masculine singular accusative is `bernom`; nominative plural is
`bernes`. The English word “boy” maps to `bernos` in the shared JSON.
An external ChapterGuides Gin instance will adopt it on the next validated
public-repository refresh or the local **development-only** forced-sync route.

## Vocabulary-only live synchronization: `memsom` (“meat”)

The canonical dictionary already included `memsom` (neuter noun, “meat”)
and the regular verb `eden` (“eat”). The English sentence translator did
not know how to turn the *meaning* “meat” into the object `memsom`.
The shared `english_nouns` mapping now includes `"meat": "memsom"`,
and `mass_nouns` includes `"meat"` to render natural English.

Examples: “I eat meat.” and “I eat the meat.” both yield
`Ego edo memsom.`; the reverse yields “I eat meat.” The limited
Go translator currently does not preserve definiteness for these objects.
This is a **JSON-only upstream change**, intentionally leaving the CSV and
ChapterGuides binary unchanged to prove that hot-reload responds to
shared lexical JSON checksum changes.
