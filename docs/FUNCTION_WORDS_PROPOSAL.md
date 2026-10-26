# Function words: current status and candidates

**Status: discussion only, 2026-10-26.** Nothing in the "candidates" section is implemented by the translator or added as an official headword until explicitly approved.

## Existing Neva core (provisionally established)

| Function | Form | Status |
|---|---|---|
| distal demonstrative / 3rd-person pronoun | so (M), sa (F), tod (N) | Singular citation forms established; complete case and plural paradigms not settled |
| who / what | kis / kid | Basic interrogative forms established; genitive, dative, plurals not settled |
| where / when / how | ku / koda / komo | Invariable interrogatives established in the working grammar |
| mark yes/no question | ka | Established |
| and | ke | Established, independent rather than enclitic |
| not | ne | Established |

PIE *kʷís* / *kʷíd* provides the historical model for "who / what"; PIE *so / seh₂ / tod* for demonstratives. These are adaptations, not a claim of identical inherited case paradigms.

## Candidate connectives for review

| English | Candidate Neva | Reason | Status |
|---|---|---|---|
| **or** | **ve** | Inspired by reconstructed PIE disjunctive *wē* (compare Sanskrit vā, Latin -ve). Neva w > v and vowel length removed. Use as independent word by analogy with ke. | PROPOSED |
| **but / yet** | **at** | From the PIE *h₂et-* connective family, with Latin at "but, whereas" and related Indo-European particles as examples. Short and phonologically simple. | PROPOSED |
| **however / nevertheless** | **tamen** | Borrowing-inspired from Latin tamen "nevertheless." Natural spelling/phonotactics; less directly traceable to a single securely reconstructed PIE connective. Could also be formed from at plus an intensifier instead. | PROPOSED |
| **and** | **ke** | Established: independent analogue of PIE clitic *-kʷe*. | ALREADY CORE |
| **because** | TBD | Prefer a transparent compound of an explanatory/cause word rather than inventing an unattested direct PIE conjunction. | OPEN |
| **if** | TBD | Needs conditional clause grammar and a comparative basis; do not coin casually. | OPEN |
| **although** | TBD | Can be a phrase/compound once concession and contrast morphology is defined. | OPEN |

None of these require additional phonemes. The forms ve, at, tamen avoid diphthongs.

## Syntax to approve separately

- Use free, preverbal or interclausal words in SVO order for ke/ve/at, even where reconstructed PIE historically used *postposed clitics*.
- Decide whether 'however' is a sentence adverb (e.g. tamen + comma + main clause) or a conjunction connecting two clauses; these are not identical uses in English either.
- Demonstratives currently double as third-person pronouns; define near-vs-far forms ('this/that'), singular/plural and case tables before automated translation of deixis.
- Relative pronouns ('who/which/that') are distinct from interrogative kis/kid in actual complex clauses; define separately before enabling relative-clause translation.

## Comparative references

- University of Texas Indo-European Syntax, verbal modifiers/particles: https://lrc.la.utexas.edu/books/pies/4-verbal-mods
- PIE interrogative morphology: https://en.wiktionary.org/wiki/Appendix%3AProto-Indo-European/k%CA%B7is
- PIE contrast particles: https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82et-
- Latin at (conjunction): https://en.wiktionary.org/wiki/at#Latin

**No function-word candidates in this document are automatically recognized by scripts/neva_translate.py.** Unknown/connective-heavy sentences return an unsupported-input error for now.
