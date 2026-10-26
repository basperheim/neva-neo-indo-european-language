# Demonstratives, interrogatives, and remaining grammar decisions

**Status:** unapproved design choices (2026-10-26). This is a proposal, **not** a change to the grammar, dictionary headwords, declension code, or translator. The previously adopted third-person forms `so/sa/tod`, interrogatives `kis/kid`, and question particle `ka` remain active. The preposition **`pro`** (“for, for the sake of, on account of”) has separately been approved and is part of the lexicon.

## Historical basis and design constraints

- PIE had a demonstrative `*so / *seh₂ / *tod` whose historical semantics were broader than a compulsory modern near/far opposition. Neva **chooses** to use `so/sa/tod` for *that* and for ordinary third-person reference; this is a constructed-language semantic standardization.
- PIE deictic `*ḱe-` “this/here” is a defensible inspiration for Neva **sh-**, using the existing `ḱ → sh` adaptation. It is **not** the same source as Neva `ke` “and,” inspired by PIE enclitic `*-kʷe`.
- PIE *g⁽ʰ⁾e* is an **intensifier**, so its use to mark literal proximity would be an explicit semantic innovation, not an inherited contrast.
- PIE `*kʷís / *kʷíd` motivates `kis` (who) / `kid` (what). The historical *kʷi-* vs *kʷo-* pronominal/adjectival distinction motivates a separate *which* series.
- Keep three genders, four cases, singular/plural, regular pronunciation, and penultimate stress. Allow natural case syncretism, as already happens in nouns.

Historical grounding: [UT Indo-European Syntax, categories](https://lrc.la.utexas.edu/books/pies/5-categories); [PIE interrogatives](https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European/k%CA%B7is); [comparative Germanic demonstratives](https://tile.loc.gov/storage-services/master/gdc/gdcebookspublic/20/18/03/18/62/2018031862/2018031862.pdf); [PIE proximal root](https://lrc.la.utexas.edu/lex/master/0990).

## Decision DEM: three demonstrative approaches

### A — distinct agreeing proximal series (RECOMMENDED)

Treat `so / sa / tod` as distal *that* and propose `shos / sha / shod` as proximal *this*. Both can function as free-standing demonstrative pronouns or as **gender/number/case agreeing determiners** before nouns.

| Nominative | Masculine | Feminine | Neuter |
|---|---|---|---|
| Proximal singular | **shos** | **sha** | **shod** |
| Distal singular | so | sa | tod |
| Proximal plural | **shes** | **shas** | **sha** |
| Distal plural (existing pronominal) | toi | tai | ta |

Examples:
- `shod genom` = this child; `tod genom` = that child.
- `sha mathera` = this mother; `sa mathera` = that mother.
- `shes vulkes` = these wolves; `toi vulkes` = those wolves.
- `sha gena` = these children; `ta gena` = those children.

**Provisional *full proximal paradigm***, entirely constructed through Neva regularization and **not** a PIE reconstruction:

| Case | M sg. | F sg. | N sg. | M pl. | F pl. | N pl. |
|---|---|---|---|---|---|---|
| Nominative | shos | sha | shod | shes | shas | sha |
| Accusative | shom | sham | shod | shons | shans | sha |
| Genitive | shosio | shas | shosio | shon | shon | shon |
| Dative | shoi | she | shoi | shois | shes | shois |

Examples: `Vido shom vulkom` = I see this wolf; `Bero vodrom she mathere` = I carry water to this mother. `She` is the **feminine dative form** under option A, not an invariant particle.

The distal series currently serves as third-person pronouns. A separate **declension of the distal forms** must be audited for consistency against the previously published object/possessive forms before freezing the determiner paradigm; do **not** generate an assumed full table from ordinary noun endings. Dative `sai` (“to her”) in earlier drafts is not automatically superseded by `se`; that must be resolved deliberately.

### B — invariant proximal particle

Propose `she` (“this/these”) before a noun, whatever its gender/case/number:
- `she genom` = this child
- `she mathera` = this mother
- `she gena` = these children

Retain `so/sa/tod` for “that.” Few rules and no new agreement tables, but loses some deliberately retained PIE pronominal morphology; `she` would have the same spelling as the *feminine dative* in Option A, so **do not adopt both systems**.

### C — old pronouns plus emphatic particle

Use `ge` before `so/sa/tod`, conveying “that very ...” and optionally extending it to “this.”
- `ge tod genom` = that very child (proposed reanalysis: this child)

Historical use of PIE *g⁽ʰ⁾e* supports intensity, **not** deictic near/far distance. This is semantically weaker than Option A.

## Decision WHICH: how to say “which?”

This is separate from **independent** interrogative `kis` “who” and `kid` “what”, which the working grammar already uses.

1. **Option W1 (RECOMMENDED)**: agreeing adjectival `kinos` (M), `kina` (F), `kinom` (N), plural `kines / kinas / kina`. A Neva *kʷi-* inspired stem plus **analogical -n-** and regular adjective endings. The *-n-* is invented for clarity/phonotactics, not a claimed PIE suffix. E.g. `Kinos eshvos?` = Which horse? `Kina mathera?` = Which mother? `Kinom genom?` = Which child?
2. **Option W2**: invariant `ki` before any noun. Very simple, but no agreement: `ki eshvos?`, `ki mathera?`, `ki genom?`.
3. **Option W3**: `kos / ka / kod` based more transparently on PIE adjectival *kʷo-*. But **`ka` clashes with Neva's yes/no question marker**, leading to avoidable parser ambiguity, so not recommended.

**Recommendation:** W1 preserves gender agreement like Option A; distinguish free-standing `kis/kid` from attributive `kinos/kina/kinom`. Don't conflate relative “who/that” with interrogative “who/what” without a separate relative-clause policy.

## Remaining function-word decisions, in priority order

- **REL:** Relative clause markers ("the mother **who** carries water", "the computer **that** I have"). PIE had *y-* and *kʷ-* relative strategies in different branches. Choose a Neva strategy explicitly.
- **COND:** Conditional `jaba` (“if”) is proposed, Germanic-inspired, not adopted. Need verb tense and clause ordering behavior.
- **CONNECT:** `atoge` (“however/nevertheless”) proposed from `at + o + ge`. Decide sentence-adverb behavior and punctuation. Keep English “however” = “in whatever manner” distinct.
- **CAUSE:** `pro kid` can mean “for what?/why?” and `pro tod` “for that reason/because of that.” These are **prepositional phrases**, not a general subordinating `because` that can directly introduce any clause.
- **DEICTIC:** A separate distal *that* series is an intentional Neva simplification: old PIE `*so` may also have meant *this*, depending on context. Pronoun *this* vs determiner *this* uses should be specified consistently.

## Prioritized roadmap: what is left for usable Neva?

**Priority 1 — close the core grammar**
1. Choose DEM + WHICH and document singular/plural case tables; decide gender/case declension for third-person pronouns and demonstratives consistently.
2. Lock interrogative case forms (`kis/kid`, who/what/whose/to whom); distinguish interrogatives, relatives and indefinites.
3. Adopt/reject `jaba`, `atoge`, causal subordinators, `pra`, and the remaining preposition/case roles.
4. Define relative clauses, subordinate clause word order, comparison (bigger/biggest), passive voice, and reflexive constructions. Decide what to leave periphrastic rather than inflected.

**Priority 2 — make language data dependable**
5. Review vowel sequences, stress on long compounds, laryngeal coloring and lexical sound-change exceptions. No destructive rederivation of approved vocabulary.
6. Audit PIE roots, semantic glosses, gender evidence, derivational suffixes, irregular verbs/nouns, and compound head agreement. The 801 entries are a *working candidate lexicon*, not 801 independently reconstructed PIE roots.
7. Expand basic daily vocabulary and idioms, count/time expressions and register; build a sentence corpus with translation and expected IPA.

**Priority 3 — implement the resulting language**
8. Refactor the Python translator toward an explicit parse tree / tokenization, show ambiguity, support conjunctions, questions and new pronouns without guesswork; maintain `--strict`.
9. Add offline pronunciation/TTS using eSpeak NG, optionally Piper, with careful phoneme and stress mapping.
10. Pin a validated dictionary export for the planned lightweight Go/Gin ChapterGuides API and Astro interface; deploy only when user explicitly requests it.

**Explicitly not required:** bringing back all eight PIE noun cases, the dual, productive noun ablaut, historical laryngeal consonants, grammatical gender exceptions for every new compound, or hosted AI translation. Those would work against Neva's design goals.

## Vote request

Choose a demonstrative **A/B/C** and interrogative adjective **W1/W2/W3**. The recommendation is **A + W1**. None has been inserted into the canonical grammar or translator until confirmed.
