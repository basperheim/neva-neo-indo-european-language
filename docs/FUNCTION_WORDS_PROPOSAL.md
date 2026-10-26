# Function words: current status and candidates

**Status (2026-10-26):** The user approved **at** “but/yet” and **ve** “or” alongside existing **ke** “and”; these are now official dictionary entries. Other words in this document remain candidates, not implemented or automatically supported by sentence translation.

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
| **or** | **ve** | Inspired by PIE disjunctive *wē* (compare Sanskrit vā, Latin -ve). Neva w > v and vowel length removed; independent word. | **ADOPTED / dictionary** |
| **but / yet** | **at** | From PIE *h₂et-* connective family, compare Latin at "but, whereas" and Sanskrit atha. Short and phonologically simple. | **ADOPTED / dictionary** |
| **however / nevertheless** | **atoge** | New proposal: **at** “but” + linking **-o-** + **ge** from PIE intensifier *g⁽ʰ⁾e* “indeed, in fact.” Pronounced /a.ˈto.ge/. A Neva compound, not an attested PIE conjunction; avoids Latin/Esperanto *tamen*. | **PROPOSED** |
| **and** | **ke** | Established: independent analogue of PIE clitic *-kʷe*. | ALREADY CORE |
| **because** | **pro tod** (reason phrase) | Candidate “for that [reason], because of that,” with **pro** from PIE *pró* “forward/for” + **tod** “that.” This is **not automatically a clause conjunction** and must not substitute for all uses of “because.” | **PROPOSED** |
| **if** | **jaba** | Suggested from Proto-Germanic *jabai / *ibai* “if,” associated with *jabą* “condition.” Neva /ˈja.ba/ removes the diphthong; this is a **Germanic-inspired borrowing/adaptation**, not a reconstructed PIE conditional. Conditional-clause syntax still needed. | **PROPOSED** |
| **although** | TBD | Can be a phrase/compound once concession and contrast morphology is defined. | OPEN |

None of these require additional phonemes. Atoge, jaba, pro and tod are spelled with ordinary Neva vowels and consonants. **pro kid** could literally mean “for what?” or “why?”, but the interrogative “why?” and causal subordinating “because” are not interchangeable.

## Syntax to approve separately

- **Approved usage:** ke, ve and at are independent connectives, despite PIE postposed clitics in part of their historical background. Their use in unrestricted clause coordination still needs full sentence parser rules.
- Decide whether **atoge** (proposed) functions as a sentence adverb or as an interclausal coordinator. Avoid confusing English “however” meaning “nevertheless” with “however” meaning “in whatever manner.”
- Demonstratives currently double as third-person pronouns. PIE *g⁽ʰ⁾e* is an **intensifier**, not intrinsically a proximal “this”; candidate Neva **ge** “indeed/the very” might reinforce an existing demonstrative but is not itself a determiner. PIE *ḱe* is a **different, genuinely deictic** “this/here” particle and a stronger starting point for a proximal series. Do not conflate the two roots. Define near/far forms, plural and case agreement first.
- Relative pronouns ('who/which/that') are distinct from interrogative kis/kid in actual complex clauses; define separately before enabling relative-clause translation.

## Comparative references

- University of Texas Indo-European Syntax, verbal modifiers/particles: https://lrc.la.utexas.edu/books/pies/4-verbal-mods
- PIE interrogative morphology: https://en.wiktionary.org/wiki/Appendix%3AProto-Indo-European/k%CA%B7is
- PIE contrast particles: https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%82et-
- Latin at (conjunction): https://en.wiktionary.org/wiki/at#Latin

**Implementation scope:** ke already works for a limited pair of direct objects in the experimental translator. at and ve are accepted **dictionary words**, not yet parsed as general sentence connectives; other candidates remain unrecognized. CLI now preserves unsupported sentences and warns by default, or errors with `--strict`. This avoids pretending full coordination is implemented.
