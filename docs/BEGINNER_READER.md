# Reading Neva: Beginner Conversations, Directions, and a Short Tale

**Status:** Neva 1.4 beginner reader (2026-10-26). Every Neva sentence here is a **constructed-language example**, not reconstructed PIE. The phrasebook contains a few conventional expressions; the remaining examples use ordinary Neva grammar. The sentence corpus lives in [`data/sentence_corpus.tsv`](../data/sentence_corpus.tsv), and automated tests verify the written English translations.

## Quick start

From the repository root:

```bash
git pull --ff-only origin master
python3 scripts/neva.py examples --limit 10
python3 scripts/neva.py examples --category Greeting
python3 scripts/neva.py examples --category Directions
python3 scripts/neva.py examples --category Story
python3 scripts/neva.py translate 'Jaba beres vodrom, vel kapo vodrom.'
python3 scripts/neva.py translate --from en --to neva 'I see a mother who carries water.'
python3 scripts/neva.py compare mezos --degree superlative --gender F
python3 scripts/neva.py decline-relative josa --case accusative
python3 -m unittest discover -s tests -v
```

By default `translate` means Neva → English. For English → Neva, specify `--from en --to neva`. Unknown or unsupported sentences are echoed *unchanged* with a warning; add `--strict` to produce a nonzero error instead. The translator isn't intended to infer unknown grammar or invent words.

## Basic greetings

| English | Neva | Comment |
|---|---|---|
| Hello! | **Vese!** | Conventional Neva greeting from an existing “well” adverb |
| Good day! | **Vesom deinom!** | Neuter adjective + neuter day |
| How are you? | **Komo es?** | Literally “How are [you]?” |
| I am well. | **Em vese.** | Subject pronoun omitted |
| Yes. | **Ja.** | Established affirmation |
| No. | **Ne.** | Conventional negative answer |
| Good night! | **Vesa nokta!** | Feminine adjective agrees with *nokta* “night” |

**Two-person exchange**

> **A:** Vese! — Hello!  
> **B:** Vese! — Hello!  
> **A:** Komo es? — How are you?  
> **B:** Em vese. — I am well.  
> **A:** Vesom deinom! — Good day!

These aren't ancient PIE greetings. They are modern Neva conventions: short, pronounceable, and consistent with the current vocabulary. We still need a natural word or fixed idiom for “thank you,” “please,” and “goodbye” instead of inventing dubious etymologies.

## Asking directions

| English | Neva |
|---|---|
| Where is the house? | **Ku est domom?** |
| Where is the door? | **Ku est dhverom?** |
| Where is the road? | **Ku est pontos?** |
| Go to the house! | **Ie ad domom!** |
| Go to the door! | **Ie ad dhverom!** |
| Go through the door! | **Ie per dhverom!** |
| I go toward the door. | **Io ad dhverom.** |

The commands and *ku* questions are explicitly supported conversational conventions; for other combinations, the general translator understands a **subset** of verbs with preposition + accusative. `ad` means “toward,” `per` means “through,” and `en` means “in/into.” Locations don't need a new locative case. We have **not** yet standardized “left,” “right,” “straight ahead,” or the cardinal directions. That is a useful next vocabulary milestone.

## A short story: the wolf and the horse

This is a deliberately elementary mini-story using our existing words, comparative endings, and a conditional. It is not an ancient fable.

| Neva | English |
|---|---|
| **Vulkos videth eshvom.** | The wolf sees a horse. |
| **Eshvos videth vulkom.** | The horse sees a wolf. |
| **Shos vulkos est mezoteros apo som eshvom.** | This wolf is bigger than that horse. |
| **Jaba eshvos videth vulkom, eshvos ieth ad domom.** | If the horse sees a wolf, the horse goes toward the home. |
| **Vulkos ne ieth ad domom.** | The wolf does not go toward the home. |

The eventual *fable* genre needs more basic vocabulary for motives, actions, emotion, and morals (for instance “fear,” “help,” “wise,” “speak,” “tell”). It's better to build that vocabulary transparently than to pretend a five-sentence scene is a literary epic.

## Why these forms work

**Cases:** `vulkos` “wolf” as subject → `vulkom` when it is the object of *see*. `eshvos` “horse” → `eshvom` in the accusative.

**Pronouns and demonstratives:** `shos vulkos` = “this wolf” (masculine nominative). `som eshvom` = “that horse” (masculine accusative). Those two agreeing modifiers use different case forms.

**Verb person:** `videth` = he/she/it sees; `ieth` = he/she/it goes; `beres` = you carry; `kapo` = I have.

**Conditional:** `jaba [normal present-tense clause], [normal clause]`. No special subjunctive needed for ordinary real/likely conditions.

**Cause:** `kod` introduces a full explanatory clause; `pro tod` means “for that reason” and is a prepositional phrase rather than a finite-clause conjunction.

**Comparison:** `mezos` “big” → `mezoteros` “bigger” → `mezistos` “biggest.” Use `apo` + accusative in the elementary “bigger than…” pattern. Comparative/superlative adjectives keep ordinary gender, number, and case endings.

**Relative clause:** `Vido matheram josa bereth vodrom.` = “I see a mother who carries water.” Although *matheram* is accusative in the main clause, *josa* is nominative because it is the subject of *bereth* in its own clause.

## Relative and comparative examples

| Neva | English |
|---|---|
| **Vido matheram josa bereth vodrom.** | I see a mother who carries water. |
| **Vido vulkom jos videth matheram.** | I see a wolf that sees a mother. |
| **Jaba beres vodrom, vel kapo vodrom.** | If you carry water, I will have water. |
| **Bero vodrom kod mathera ne bereth vodrom.** | I carry water because the mother does not carry water. |
| **Shos vulkos est mezoteros.** | This wolf is bigger. |
| **Shos vulkos est mezoteros apo som vulkom.** | This wolf is bigger than that wolf. |

## Reader pronunciation hints

- `th` = /θ/ as in *think*; `dh` = /ð/ as in *this*; `sh` = /ʃ/ as in *ship*.
- `j` = /j/ as in English *yes*; `y` = /y/ as in German *über*.
- Each word's **second-to-last syllable** receives the main stress, including long compounds.
- `oi` = /oi̯/ like *oy* in *boy*. `osio` is /o.si.o/, not a single vowel glide.
- Neva has no silent letters or obligatory English-like articles.

For IPA try `python3 scripts/neva.py ipa 'Vulkos videth eshvom.'`. The IPA tool is a broad approximation and still needs human pronunciation review for long compounds and edge-case syllabification.

## What the experimental translator can and cannot do

**Can:** understand a curated set of verbs, four noun cases, demonstrative noun phrases, regular comparative/superlative adjectives, a **single** relative clause after an object, a simple conditional or causal **two-clause** sentence, very small coordinated clauses, basic prepositions, and a few everyday idioms.

**Cannot reliably:** parse unrestricted English or Neva, translate nested relative clauses, infer omitted discourse context, translate arbitrary interrogatives, place relative pronouns in every possible syntactic position, use an unreal conditional mood, or translate novel idioms by guessing. Unknown material is echoed unchanged (or rejected with `--strict`), not silently fabricated.

You can use `examples` to browse the corpus and `lookup` to explore the working lexicon. The vocabulary currently contains 812 candidate headwords, *not* 812 independently verified reconstructed PIE lexemes.
