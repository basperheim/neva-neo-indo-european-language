# Neva everyday vocabulary and English high-frequency coverage

**Status: working lexicon expansion, 2026-10-26.** The canonical CSV contains **828 distinct headwords**, including **449 nouns**, with all noun genders marked by the usual Neva rules. This is **not** a verified list of 828 PIE roots. Source-based adaptations, modern Neva derivations, inherited-inspired extensions, and uncertain coinages are labeled separately.

## Why "language" is `denegva`

Already established Neva `denegva` “tongue” (feminine) comes from the proposed PIE *dn̥ǵʰwéh₂s* tongue. It now has the **additional** conventional meaning **“language”**, just as Latin `lingua` means tongue and language. Neva `vekom` (“speech, utterance”) and `verdom` (“word”) remain distinct. You do not need to invent a different root.

| Case | Singular | Plural |
|---|---|---|
| Nominative | denegva | denegvas |
| Accusative | denegvam | denegvans |
| Genitive | denegvas | denegvon |
| Dative | denegve | denegves |

Spoken stress: de-**NEG**-va (assuming established penultimate stress). English *language* → Neva `denegva` is an **exact headword lookup**, not a complete grammatical sentence.

```bash
python3 scripts/neva.py translate --from en --to neva language
# denegva
python3 scripts/neva.py translate denegva
# tongue / language
python3 scripts/neva.py translate --from en --to neva cat
# miava
python3 scripts/neva.py decline denegva F --case dative --number singular
# denegve
```

The standalone translator can now use dictionary entries and their **exact comma-separated English glosses**. If two Neva headwords could match a bare English word (for example “bear” as an animal versus the verb “bear/carry”), it reports **ambiguity** rather than silently choosing. Complex grammar and idioms still need the sentence translator. When a word is unsupported, ordinary CLI passthrough and `--strict` behavior remain unchanged.

## Animals

| Neva | English | Gender | Etymology status |
|---|---|---|---|
| dhorom | animal | N | Existing base word |
| shvonos | dog | M | Existing inherited-inspired base |
| vulkos | wolf | M | Existing inherited-inspired base |
| eshvos | horse | M | Existing inherited-inspired base |
| gava | cow | F | Existing inherited-inspired base |
| avisa | bird | F | Existing inherited-inspired base |
| peiskom | fish | N | Existing inherited-inspired base |
| ovisa | sheep | F | Adapted from reconstructed *h₂ówis* f., with regular Neva -a |
| gansa | goose | F | Adapted from *ǵʰh₂éns* f., regularized |
| musos | mouse | M | *mūs*-inspired form, gender/provenance provisional |
| susos | pig, swine | M | *suH-* inherited root; **Neva masculine default** because older gender varies |
| kapros | he-goat | M | *kápros*-inspired; historical PIE status **debated** (possible later loan) |
| artos | bear | M | *h₂ŕ̥tḱos*-inspired but remodeled away from difficult clusters |
| miava | cat | F | **Neva onomatopoeic invention**, not a reconstructed PIE term |

**Important:** New animals do not establish historical PIE genders merely by their Neva endings. That information is tracked in the dictionary, and several historical forms need follow-up.

Sources: [PIE sheep](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C3%B3wis), [goose](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%82%C3%A9ns), [pig](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/suH-), [goat](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%C3%A1pros), [bear](https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82%C5%95%CC%A5t%E1%B8%B1os).

## Household items and tools

Rather than invent a second term when an existing Neva `-otrom` **instrument** is semantically appropriate, we've **lexicalized** an ordinary modern meaning. These are functional coinages, **not direct PIE objects**.

| Neva | Everyday English | Type |
|---|---|---|
| sedotrom | chair, seat | New: sitting instrument from `seden` |
| svepotrom | bed | New: sleeping instrument from `svepen` |
| dhotrom | table, stand | New: place/put support from `dhen` |
| kertotrom | knife, cutting tool | Existing cutting-tool word, meaning extended |
| plakotrom | hammer, striking tool | Existing striking-tool word, meaning extended |
| piotrom | cup, drinking vessel | Existing drinking-tool word, meaning extended |
| pekotrom | pot, cooking vessel | Existing cooking-tool word, meaning extended |
| edotrom | eating utensil | Existing broad eating implement |
| vodrokapotrom | bucket, water vessel | Existing transparent compound |
| domolevkom | lamp, house light | Existing compound |
| domopokom | stove, house hearth | Existing compound |
| gerbotrom | pen | Existing writing instrument |
| menotrom | computer | Existing thinking instrument |

These compound instrument forms take the **neuter** case endings. E.g. `sedotrom` chair → plural **sedotra**. We're not claiming every cutting tool is *literally* a knife or every ancient hearth a modern kitchen stove; these are deliberately conventional senses.

## Time, and qualities

| Neva | Meaning | Note |
|---|---|---|
| nu | now | Short inherited-inspired temporal particle |
| nudein | today | Modern Neva 'now-day' adverb |
| deinom | day | Existing N |
| nokta | night | Existing F |
| avosa | dawn, early morning | Adapted from *h₂éwsōs* f. |
| vesperos | evening | PIE-based source with debated internal analysis |
| menos | moon; month | Older noun extended to calendrical meaning |
| vetom | year | Existing N |
| septemodeinom | seven-day week | **Modern seven-day calendar compound**, N |

Other adjectives **already** present include `leukos` bright, `noktos` dark, `tepos` warm, `gelos` cold, `grevos` heavy, `levos` light in weight, `dlongos` long, `mregos` short, `meios` small, `vesos` good, `dusos` bad, and `senos` old. The new adjective `zeninos` means **wise/knowledgeable**, a regular Neva relational derivative of `zenen` (“know”); the meaning is modern lexicalization, not a separately proven PIE adjective.

**Still missing**: tomorrow/yesterday, times of day beyond dawn/evening, left/right/straight, week days, season names, certain household items (window, spoon, fork), and idioms such as *please*, *thank you*, and *goodbye*. These are good next additions, but each should have an examined source and inflection class.

## The Oxford English Corpus top-100 audit

The Wikipedia [Most common words in English](https://en.wikipedia.org/wiki/Most_common_words_in_English) page lists 100 **frequent English lexemes**, many with very different grammatical uses. We've recorded **every ranked entry** in [`data/english_top100_coverage.tsv`](../data/english_top100_coverage.tsv).

| Audit status | Count | What it means |
|---|---:|---|
| `lemma` | 43 | A basic Neva dictionary headword exists |
| `grammar` | 23 | Case, affix, agreement, or multi-form construction expresses its grammatical function |
| `partial` | 7 | At least one sense is expressible, but the English term has further meanings |
| `gap` | 27 | No reliable general equivalent/rule yet |
| **Total** | **100** | **100/100 entries assessed; not 100/100 translated** |

Use the new command:

```bash
python3 scripts/neva.py coverage --limit 25
python3 scripts/neva.py coverage --status grammar
python3 scripts/neva.py coverage --status gap
```

Some examples:
- **the / a / an**: Neva *deliberately* has no obligatory article. Do not invent a nominal suffix for these.
- **of**: often a **genitive** relationship (`-osio, -as` etc.), not a universal preposition.
- **to**: direction `ad`, beneficiary/recipient dative, or verb infinitive `-en`; these are **not synonyms**.
- **would/could/can**: modal and irrealis grammar genuinely needs decisions.
- **English “at” (location)** remains a **gap**: Neva `at` already means “but.”
- **“that”**: demonstrative `so/sa/tod` vs relative `jos/josa/jod`, never one universal suffix.
- **than**: `apo` + accusative in comparative constructions.
- **most**: adjective degree `-ist-` exists, but quantifier “most people” is **not** automatically covered.

### Next priorities

1. Resolve the most valuable **27 top-100 gaps** by grammar family, particularly *can/would*, *some/any/all/other*, *at/on/out*, *there/then*, *also/only*, *about/by*, and ordinal *first*. Avoid a one-English-word/one-Neva-word assumption.
2. Expand a **small useful animal + everyday objects vocabulary** with etymology/confidence flags; prioritize collocations over dozens of generic compounds.
3. Create everyday conversational idioms and test them against a beginner corpus; add nouns for ordinary household environments and spatial directions.
4. Continue a PIE **source audit**, distinguishing firmly reconstructible bases from later family-level sources and Neva analogies.

The current `translate` CLI is a **bounded language-learning prototype**. Exact headword lookup helps with single words, but cannot infer case, article use, or the intended sense of polysemous English words.
