# Experimental offline translator — MVP

**Status:** limited grammar prototype, not general-purpose machine translation. It translates only confidently supported structures, **passes unsupported input back unchanged by default** (with a warning on stderr), and can still reject unsupported constructs with `--strict`. It runs on Python 3.10+ standard library with no hosted service, Google API, LLM, or network access.

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

    python3 scripts/neva.py translate —from en —to neva "I carry water."
    # Ego bero vodrom.

    python3 scripts/neva.py translate —from en —to neva "The mother sees a wolf."
    # Mathera videth vulkom.

    python3 scripts/neva.py translate —from en —to neva "I have carried water."
    # Ego kapo beroto vodrom.

    # Phrasebook: English -> Neva
    python3 scripts/neva.py translate —from en —to neva 'Hello!'
    # Vese!

    python3 scripts/neva.py translate —from en —to neva 'Good day!'
    # Vesom deinom!

    python3 scripts/neva.py translate —from en —to neva 'How are you?'
    # Komo es?

    # Phrasebook: Neva -> English
    python3 scripts/neva.py translate 'Vesom deinom!'
    # Good day!

    # Unrecognized text: unchanged, warning on stderr
    python3 scripts/neva.py translate 'Hello!'
    # Hello!  (no conversion: default source is Neva)

    # Old strict behavior, exit status 2 on unsupported input
    python3 scripts/neva.py translate —strict 'Bero inventedword.'

    python3 -m unittest discover -s tests -v

The default is Neva to English. `--from` takes `neva` or `en`, and `--to` takes `en` or `neva`. Only distinct direction pairs are supported. Use `--strict` to restore the former nonzero exit code for unknown grammar. Without `--strict`, unsupported sentences are printed **byte-for-byte as passed to the argument** with a warning on stderr. This avoids guessing meaning; it does **not** attempt unsafe token-by-token translation of a partly unknown clause. Run `translate --help` for flags.

## Supported grammar subset

Neva to English:
- Approved agreeing demonstrative and interrogative-determiner noun phrases: `shos/sha/shod`, `so/sa/tod`, `kinos/kina/kinom`, inflected for noun gender, case and number. Recognizes `sam matheram` as a determiner+noun combination rather than always treating `sam` as a standalone object pronoun.
- Exactly one simple clause, optionally ended by a period, exclamation mark, or question mark.
- A small curated set of common verbs in present/past, future with vel, negation with ne, optional explicit subject pronouns, basic nominative noun subjects.
- Perfect with kapen + -oto participle (Kapo beroto vodrom).
- Regular case endings and explicitly stored irregular noun stems, including podos/ped-, across noun and adjective phrases.
- Simple direct objects (accusative), recipients (dative), and direct-object conjunction ke.
- Limited copular predicates (noun/adjective), present-tense yes/no questions with ka, and a few singular imperatives.

English to Neva:
- Selected singular `this/that` noun phrases, including forms such as `I see this wolf.` → `Ego vido shom vulkom.`; unrestricted English plurals and `which ...?` questions remain unsupported.
- Basic personal pronouns and a curated list of singular nouns, common transitive verbs, basic adjectives and recipients.
- Present, past, future, and have + past participle.
- Generates explicit Neva subject pronouns for clarity even though the language allows dropping them.

## Limitations and honesty contract

- **Bounded** conditional (`jaba`), causal (`kod`), postnominal relative (`jos/josa/jod`), and pairwise independent-clause coordination (`ke/ve/at`) are supported. **Not supported:** nested clauses, unrestricted relative syntax, free-form discourse, full English question translation, English plural noun generation, or unknown semantics.
- Translation is deterministic and lexicon-backed. **By default**, unsupported input is preserved unchanged and warns on stderr; **with `--strict`**, unsupported grammar returns `Translation unavailable: ...` and exit code 2. The underlying translation function still raises an explicit exception on unsupported input, so downstream code can make its own policy choice.
- Neva has no obligatory definite/indefinite articles. The English rendering *conventionally* uses "the" for a subject count noun and "a" for an object count noun; neither definiteness nor indefiniteness is explicitly encoded by the Neva source.
- Many of the 798 dictionary headwords are provisional derived words and compounds. Glosses are not always idiomatic.
- Noun case syncretism can produce more than one theoretical interpretation. The current small parser uses case position and agreement; it does not model full ambiguity.
- Some etymological source adaptations deliberately preserve recognizable forms such as genom; phonemic pronunciation remains consistent after the Neva word is chosen.

This Python implementation is the reference behavior for a later pinned Go dictionary/morphology export for ChapterGuides. No Python interpreter or AI inference is required on the Alpine production VM.

## Status of function words

Core forms defined: proximal demonstratives shos/sha/shod ("this"), distal demonstratives so/sa/tod ("that"), attributive interrogatives kinos/kina/kinom ("which"), independent interrogatives kis/kid/ku/koda/komo, question marker ka, conjunctions ke ("and"), **ve ("or")** and **at ("but/yet")**, negation ne, and future marker vel. The translator currently parses `ke` only in a constrained direct-object coordination pattern; `ve`/`at` are recognized dictionary entries but not yet general clause conjunction grammar.

Not fully finalized: independent interrogative `kis/kid` case paradigms, general wh-questions, long-distance relative syntax, nested subordinate clauses, and counterfactual conditional mood.

Already adopted: `jaba` ("if"), `kod` (full-clause "because"), and relative pronouns `jos/josa/jod`. Still unapproved: "however" (`atoge`), "although," and more advanced clause-scope rules. **Atoge** ("however") remains a candidate. The approved **pro tod** is a causal phrase ("for that reason"); **kod** is the full-clause causal connector. None is a fully implemented conjunction in the translator. See [function words](FUNCTION_WORDS_PROPOSAL.md).

Neva ke is an independent connective, inspired by PIE enclitic *-kwe (whose reflexes appear throughout early Indo-European languages). The independent position is a deliberate simplification.

See the root NEVA_OVERVIEW.md for the broader morphology.

## Greetings and everyday expressions (provisional)

The phrasebook `scripts/neva_phrases.py` maps a few ordinary conversational expressions without requiring the complete sentence parser:

| English | Neva | Note |
|---|---|---|
| Hello! / Hi! | **Vese!** | Conventional greeting adapted from *vese* "well"; a Neva coinage |
| Good day! | **Vesom deinom!** | *vesom* agrees with neuter *deinom* "day" |
| How are you? | **Komo es?** | *komo* "how" + second-singular *es* "are" |
| I am well. | **Em vese.** | First-singular *em* "am" + adverb *vese* |

The phrasebook accepts optional trailing punctuation and case differences. It does **not** auto-detect the source language. To translate English, pass `--from en --to neva`.

### zsh quotation tip

In interactive `zsh`, single quotes are the safest way to pass a literal exclamation mark:

    python3 scripts/neva.py translate —from en —to neva 'Hello!'

A `dquote>` prompt indicates an **unclosed double-quoted string**. A history-expansion complaint involving `!` is separate; single quotes avoid that too. If you see `dquote>`, press Ctrl+C to cancel the incomplete command and re-enter it.

## New determiner CLI

    python3 scripts/neva.py decline-determiner shos —case accusative
    # shom
    python3 scripts/neva.py decline-determiner kina —case dative
    # kine
    python3 scripts/neva.py translate 'Vido shom vulkom.'
    # I see this wolf.
    python3 scripts/neva.py translate —from en —to neva 'I see this wolf.'
    # Ego vido shom vulkom.

One simple conditional, causal, or relative clause is now supported in the experimental translator, as documented in the [beginner reader](BEGINNER_READER.md). **Nested clauses and unrecognized syntax still require rejection or passthrough.** Do not infer unrestricted scope or idiomatic fluency from a few working examples.

## Clause, adjective, and corpus examples

```bash
python3 scripts/neva.py translate 'Jaba beres vodrom, vel kapo vodrom.'
# If you carry water, I will have water.
python3 scripts/neva.py translate 'Vido matheram josa bereth vodrom.'
# I see a mother who carries water.
python3 scripts/neva.py translate 'Bero vodrom kod mathera ne bereth vodrom.'
# I carry water because the mother does not carry water.
python3 scripts/neva.py translate 'Shos vulkos est mezoteros apo som vulkom.'
# This wolf is bigger than that wolf.
python3 scripts/neva.py decline-relative josa --case accusative
# josam
python3 scripts/neva.py compare mezos --degree comparative --gender F
# mezotera
python3 scripts/neva.py examples --category Story
```

`data/sentence_corpus.tsv` is a small, curated bilingual corpus; the test suite verifies every Neva → English row, including short story sentences and direction idioms. The `examples` command prints pairs without requiring any models or web connection. This corpus documents a *tested subset*, not the full space of possible Neva sentences.

## Translate a little story from a file

```bash
python3 scripts/neva.py translate --file examples/wolf_and_horse.neva
python3 scripts/neva.py translate --file examples/wolf_and_horse.neva --strict
```

`--file` accepts UTF-8 text with **one sentence per line**. Each line uses the same bounded parser as the interactive command. In default mode unsupported lines pass through with a warning giving the line number. Under `--strict` translation stops with exit code 2 and the source line number. A multiline paragraph or nested story is **not** understood as a whole.

## Exact standalone headwords (new)

A single known English or Neva dictionary headword now translates directly **without** requiring a full finite-verb sentence:

```bash
python3 scripts/neva.py translate --from en --to neva language  # denegva
python3 scripts/neva.py translate denegva                      # tongue / language
python3 scripts/neva.py translate --from en --to neva cup      # piotrom
```

This only matches **unambiguous individual lexical headwords** and comma-separated dictionary meanings, not English sentence word forms. For example, *bear* could be a noun or a verb, and the command deliberately flags ambiguous meanings. English articles such as *the* remain untranslatable **by design**: Neva has no obligatory article.

For a complete honest check of all 100 words in the Wikipedia/Oxford frequency list, use:

```bash
python3 scripts/neva.py coverage --limit 100
python3 scripts/neva.py coverage --status partial
```

See [vocabulary notes](VOCABULARY_EXPANSION.md) and the [ranked audit](../data/english_top100_coverage.tsv).

## Scoped frequent-English constructions (Neva v1.5)

Added to the working lexicon and CLI are the prepositions `epi` (on), `api` (at a location), `ambi` (around/beside), `ek` (outside), and `posti` (after), normally with accusative. The quantifying adjectives `somos` (some), `kvenos` (any), `solvos` (all), `alteros` (other), and ordinal `primos` (first) inflect like other positive adjectives but **are not gradable**.

Two very small analytic modal constructions are recognized by `scripts/neva_modals.py`:

- `Ego mago beren vodrom.` = I **can** carry water (present ability).
- `Ego emago beren vodrom.` = I **could** carry water (past ability).
- `Ego vela bero vodrom.` = I **would** carry water (hypothetical result).

English polite “could,” “would have,” hypothetical epistemic “could,” and general nested modal/relative clauses are **not** supported. More complex semantic scopes of “only, just, even, any, about, get, by” are only partially resolved in language design, even where a lexical entry exists.

```bash
python3 scripts/neva.py translate --from en --to neva 'I can carry water.'
python3 scripts/neva.py translate --from en --to neva 'I would carry water.'
python3 scripts/neva.py translate --from en --to neva 'I carry water on the table.'
python3 scripts/neva.py coverage --status partial
```

See [the full 27-gap decision log](ENGLISH_GAPS_RESOLUTION.md), [HANDOFF](../HANDOFF.md), and [AGENTS](../AGENTS.md).
