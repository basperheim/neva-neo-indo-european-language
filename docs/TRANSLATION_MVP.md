# Experimental offline translator — MVP

**Status:** limited grammar prototype, not general-purpose machine translation. This program rejects unknown constructions rather than inventing output. It runs on Python 3.10+ standard library with no hosted service, Google API, LLM, or network access.

## CLI usage

All commands run at the repository root (copy and paste the lines below).

    python3 scripts/neva.py translate "Kapo beroto vodrom."
    # I have carried water.

    python3 scripts/neva.py translate "Bero vodrom mathere."
    # I carry water to the mother.

    python3 scripts/neva.py translate "Mathera videth vulkom."
    # The mother sees a wolf.

    python3 scripts/neva.py translate "Ka beres vodrom?"
    # Do you carry water?

    python3 scripts/neva.py translate --from en --to neva "I carry water."
    # Ego bero vodrom.

    python3 scripts/neva.py translate --from en --to neva "The mother sees a wolf."
    # Mathera videth vulkom.

    python3 scripts/neva.py translate --from en --to neva "I have carried water."
    # Ego kapo beroto vodrom.

    python3 -m unittest discover -s tests -v

The default is Neva to English. The --from flag takes neva or en, and --to takes en or neva. Only distinct direction pairs are supported. Run translate --help for flags.

## Supported grammar subset

Neva to English:
- Exactly one simple clause, optionally ended by a period, exclamation mark, or question mark.
- A small curated set of common verbs in present/past, future with vel, negation with ne, optional explicit subject pronouns, basic nominative noun subjects.
- Perfect with kapen + -oto participle (Kapo beroto vodrom).
- Regular case endings and explicitly stored irregular noun stems, including podos/ped-, across noun and adjective phrases.
- Simple direct objects (accusative), recipients (dative), and direct-object conjunction ke.
- Limited copular predicates (noun/adjective), present-tense yes/no questions with ka, and a few singular imperatives.

English to Neva:
- Basic personal pronouns and a curated list of singular nouns, common transitive verbs, basic adjectives and recipients.
- Present, past, future, and have + past participle.
- Generates explicit Neva subject pronouns for clarity even though the language allows dropping them.

## Limitations and honesty contract

- No unrestricted relative/subordinate clauses, compound sentence parsing, full English question translation, plural English noun generation, or free-form semantics.
- Translation is deterministic and lexicon-backed. Unsupported grammar returns an explicit "Translation unavailable: ..." message and exit code 2.
- Neva has no obligatory definite/indefinite articles. The English rendering *conventionally* uses "the" for a subject count noun and "a" for an object count noun; neither definiteness nor indefiniteness is explicitly encoded by the Neva source.
- Many of the 798 dictionary headwords are provisional derived words and compounds. Glosses are not always idiomatic.
- Noun case syncretism can produce more than one theoretical interpretation. The current small parser uses case position and agreement; it does not model full ambiguity.
- Some etymological source adaptations deliberately preserve recognizable forms such as genom; phonemic pronunciation remains consistent after the Neva word is chosen.

This Python implementation is the reference behavior for a later pinned Go dictionary/morphology export for ChapterGuides. No Python interpreter or AI inference is required on the Alpine production VM.

## Status of function words

Core forms defined: distal demonstratives so/sa/tod ("that"), interrogatives kis/kid/ku/koda/komo, question marker ka, conjunction ke ("and"), negation ne, and future marker vel.

Not fully finalized: complete demonstrative and interrogative case paradigms, proximal "this", relative pronouns, and subordinate clause construction.

Not yet adopted: "but", "however", "although", "because", and "or". These should be assigned historically inspired roots through a separate morphology and etymology review before general-purpose translation expands.

Neva ke is an independent connective, inspired by PIE enclitic *-kwe (whose reflexes appear throughout early Indo-European languages). The independent position is a deliberate simplification.

See the root NEVA_OVERVIEW.md for the broader morphology.
