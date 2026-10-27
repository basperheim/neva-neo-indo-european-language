# PIE laryngeals: Neva adaptation proposal

**Status:** working historical guidance, **not a fully frozen, automatic sound-change pipeline** (2026-10-26). Any existing Neva headword takes precedence over a mechanical derivation. Etymological departures must be documented, as for `genom`.

## What the subscript notation means

The reconstructions `h₁`, `h₂`, and `h₃` are **three different PIE laryngeal consonants**, not the ordinary Neva or English letter `h` followed by numbers. Their actual ancient pronunciations are debated. The strongest evidence for their distinction is **vowel coloring**, as seen in Greek and in traces preserved by Anatolian languages.

These historical effects give Neva easy, recognizable adaptations:

| PIE environment | Broad historical consequence | Proposed Neva target |
|---|---|---|
| `e` next to `h₁` | No coloring; often lengthening when laryngeal lost | **e** |
| `e` next to `h₂` | *a*-coloring, often lengthening | **a** |
| `e` next to `h₃` | *o*-coloring, often lengthening | **o** |
| `Vh₁ / Vh₂ / Vh₃` | Often a long/colored vowel after laryngeal loss | One **short** Neva vowel, quality chosen by historical context |
| syllabic laryngeal between consonants (`CHC`) | Possible supporting vowel after consonant loss | Simplified Neva **e/a/o**, chosen case by case; never delete blindly if it creates illegal clusters |
| word-initial isolated laryngeal before a consonant | Often disappears in non-Anatolian descendants | Usually drop, repair resulting onset as necessary |
| `h₁/h₂/h₃` as independent consonants | Lost in much of non-Anatolian | **No required /h/, /x/, /χ/, /ʕ/ or silent character in Neva** |

**Important:** These are *ordered context-sensitive adaptation heuristics*, not literal global substitutions `h₂ -> a`. PIE `h₂` had no automatically identical surface realization in all phonetic environments. Likewise aspirated PIE *dʰ* is a different series altogether and should not be confused with the laryngeals.

Neva maintains six simple phonemic vowels **a e i o u y**, no phonemic vowel length, regular penultimate stress, and the possibility of documented lexical remodeling. Distinct Neva **h** /h/ can still occur in words from other sources, and is not a direct continuation of all three laryngeals.

## Specific case: PIE *preh₂-*

Reconstructed *preh₂-* denotes **before / in front** and underlies forms such as Latin *prae*. Historical *e + h₂* is associated with *ā* or related a-colored outcomes. Neva reduces its length to make a plausible simple proposal:

`*preh₂- -> [a-coloring + loss of laryngeal + no long vowels] -> pra`

**Proposed Neva `pra`** = "before; in front of," /pra/; `pr` is already a legal cluster.

This is a **proposal for a new preposition**, not yet inserted in the lexicon. The existing `per` "through/across" remains separate. `pro` "for/on behalf of" can be proposed independently from PIE *pró* (not from *preh₂-* by a universal rule).

## Counterexamples to naive replacement

- PIE *ph₂tḗr* → Neva **patheros** ("father") is *lexical remodeling*, not a trivial `h₂ -> a` string operation.
- PIE *méh₂tēr* → **mathera** ("mother") is similarly remodeled into the established Neva declension.
- PIE *h₁es-* → **es-** ("be") illustrates an uncolored `e` and loss of `h₁`.
- Neva **genom** ("child") deliberately keeps initial `g` despite a separately proposed PIE palatovelar change *ǵ → z*: phonetic regularity of Neva **does not** require historically exceptionless etymological adaptation.

## Next steps to freeze a full sound-change engine

1. Separate PIE root lexemes from source-independent Neva phonemes.
2. Record source `h₁/h₂/h₃`, their adjacent vowels and syllabic environments **before** reducing vowel length or consonant clusters.
3. Choose deterministic handling of the remaining zero grades / syllabic resonants (`r̥, n̥,` etc.).
4. Specify when `V+V` becomes hiatus, diphthong, or monophthong. Current Neva still treats `ai/ei/oi/au` as diphthongs, so the language has **not** outlawed every vowel combination.
5. Preserve a small explicit exceptions table with historic evidence and a reason for each remodeling.
6. Implement the full rule order in an independent tested script and compare it against approved headwords; never regenerate the dictionary destructively.

## References

- Scientific review of laryngeal phonetic values: https://www.sciencedirect.com/org/science/article/pii/S2212588421000028
- University of Texas PIE laryngeal theory: https://lrc.la.utexas.edu/books/piep/3-laryngeal-theory
- PIE *preh₂-* source: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/preh%E2%82%82-
- Recent discussion of *e*-coloring: https://prakrit.info/resources/papers/2014-coloring-ollett.pdf
