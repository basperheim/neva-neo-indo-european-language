# Function words: current status and candidates

**Status (2026-10-26):** Approved: `ke` “and”, `ve` “or”, `at` “but”, preposition `pro` “for”, and conditional **`jaba`** “if”. The separate deictic paradigms **shos/sha/shod** (“this”) and **kinos/kina/kinom** (“which”) are approved and implemented. Causal **`kod`** and relative **`jos/josa/jod`** are now adopted; `atoge` remains a proposal. The Python translator supports **one simple** conditional, causal or relative clause at a time, as well as limited whole-clause coordination.

## Existing Neva core (provisionally established)

| Function | Form | Status |
|---|---|---|
| distal demonstrative / 3rd-person pronoun | so (M), sa (F), tod (N) | Approved full case/number paradigm |
| proximal demonstrative | shos (M), sha (F), shod (N) | Approved full paradigm |
| attributive which | kinos (M), kina (F), kinom (N) | Approved full paradigm |
| who / what | kis / kid | Basic interrogative forms established; genitive, dative, plurals not settled |
| where / when / how | ku / koda / komo | Invariable interrogatives established in the working grammar |
| mark yes/no question | ka | Established |
| and | ke | Established, independent rather than enclitic |
| not | ne | Established |

PIE *kʷís* / *kʷíd* provides the historical model for "who / what"; PIE *so / seh₂ / tod* for demonstratives. These are adaptations, not a claim of identical inherited case paradigms.

## Candidate connectives for review

| English | Candidate Neva | Reason | Status |
|---|---|---|---|
| **or** | **ve** | Inspired by PIE disjunctive *wē* (compare Sanskrit vā, Latin -ve). Neva w > v and vowel length removed; independent word. | **ADOPTED / dictionary** |
| **but / yet** | **at** | From PIE *h₂et-* connective family, compare Latin at "but, whereas" and Sanskrit atha. Short and phonologically simple. | **ADOPTED / dictionary** |
| **however / nevertheless** | **atoge** | New proposal: **at** “but” + linking **-o-** + **ge** from PIE intensifier *g⁽ʰ⁾e* “indeed, in fact.” Pronounced /a.ˈto.ge/. A Neva compound, not an attested PIE conjunction; avoids Latin/Esperanto *tamen*. | **PROPOSED** |
| **and** | **ke** | Established: independent analogue of PIE clitic *-kʷe*. | ALREADY CORE |
| **because + full clause** | **kod** | Adopted PIE *kʷod*-inspired finite-clause conjunction, compare causal Latin *quod*. | **ADOPTED; bounded parser** |
| **because of that** | **pro tod** (reason phrase) | Approved literal construction, “for that [reason], because of that,” with **pro** from PIE *pró* “forward/for” + **tod** “that.” This is **not a clause conjunction** and must not substitute for all uses of “because.” | **APPROVED as prepositional phrase, NOT a subordinate conjunction** |
| **if** | **jaba** | Approved monophthongized form adapted from Proto-Germanic *jabai* “if”; ordinary indicative conditional clauses, without a new conjugation. | **ADOPTED (parser pending)** |
| **although** | TBD | Can be a phrase/compound once concession and contrast morphology is defined. | OPEN |

None of these require additional phonemes. Atoge, jaba, pro and tod are spelled with ordinary Neva vowels and consonants. **pro kid** could literally mean “for what?” or “why?”, but the interrogative “why?” and causal subordinating “because” are not interchangeable.

## Syntax to approve separately

- **Approved usage:** ke, ve and at are independent connectives, despite PIE postposed clitics in part of their historical background. Their use in unrestricted clause coordination still needs full sentence parser rules.
- Decide whether **atoge** (proposed) functions as a sentence adverb or as an interclausal coordinator. Avoid confusing English “however” meaning “nevertheless” with “however” meaning “in whatever manner.”
- **Approved demonstratives:** Option A and W1 are finalized; their inflected forms are in [the decision record](DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md) and `scripts/neva_determiners.py`. PIE *g⁽ʰ⁾e* is an intensifier, not the adopted proximal marker.
- **Approved:** relative pronouns `jos/josa/jod` are distinct from interrogative `kis/kid` and adjectival `kinos/kina/kinom`; their declension is in `scripts/neva_relatives.py`, with a bounded postnominal translator. Other relative positions remain to be specified.

## Comparative references

- University of Texas Indo-European Syntax, verbal modifiers/particles: https://lrc.la.utexas.edu/books/pies/4-verbal-mods
- PIE interrogative morphology: https://en.wiktionary.org/wiki/Appendix%3AProto-Indo-European/k%CA%B7is
- PIE contrast particles: https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82et-
- Latin at (conjunction): https://en.wiktionary.org/wiki/at#Latin

**Implementation scope:** The experimental translator supports a pair of direct objects linked with `ke`, **two ordinary finite clauses** linked with `ke/ve/at`, one `jaba` conditional or one `kod` causal clause, and a narrowly constrained single relative clause. Nested syntax, counterfactual mood, and general idiomatic discourse are not supported. `atoge` and other candidates are still unrecognized. CLI now preserves unsupported sentences and warns by default, or errors with `--strict`. This avoids pretending full coordination is implemented.
