# Offline speech for Neva — technical roadmap

**Goal:** pronounce Neva text faithfully using a fully local pipeline, without Google or another hosted API.

## Important distinction

Whisper (and similar speech-recognition models) is **ASR / speech-to-text**, not a speech synthesizer. It is not the component that turns Neva sentences into spoken audio. A general LLM is also not automatically a TTS engine.

## Recommended architecture

```text
Neva text
    |
    v
Tokenizer + lexicon (Python)
    |
    v
Neva grapheme-to-phoneme + stress rules
    |   current starting point: python scripts/neva.py ipa "Kapo beroto vodrom."
    v
IPA / phoneme sequence with sentence pauses
    |
    +------> eSpeak NG: immediate, wholly offline prototype, robotic quality
    |
    +------> Piper: local neural synthesizer, natural voice when phoneme inventory
                and voice model are compatible (may require adaptation/training)
    |
    v
WAV / audio file
```

## Stage 1 — deterministic pronunciation (started)

`scripts/neva.py ipa` demonstrates spelling → broad IPA and penultimate stress.

Caveat: the tokenizer uses a simplified syllable-onset algorithm. It does **not** yet encode allophony, precise IPA for every future word, phrasing, or morphology-specific stress boundaries. Keep tests for `sh`, `th`, `dh`, `y` and compound stress.

Before developing TTS, review/approve the noun morphology proposal; otherwise text generators will rapidly disagree about what words they are pronouncing.

## Stage 2 — eSpeak NG offline prototype

eSpeak NG is a lightweight open-source synthesizer with editable phoneme dictionaries and voice definitions. Install on macOS with Homebrew (`brew install espeak-ng`), then inspect available voices (`espeak-ng --voices`).

**Warning:** asking an existing language voice to read Neva orthography does not yield Neva pronunciation. A proper Neva language/dictionary or an explicitly controlled phoneme input mapping is needed; eSpeak NG phoneme notation is not the same as raw IPA strings. Initial integration should wrap a verified pronunciation mapping, not guess eSpeak's syntax.

This produces voice output quickly, but the timbre is characteristically synthetic.

References:
- https://github.com/espeak-ng/espeak-ng
- https://github.com/espeak-ng/espeak-ng/blob/master/docs/voices.md

## Stage 3 — natural neural voice

Piper is a locally running neural TTS engine with Python, CLI, and C/C++ interfaces, built around eSpeak NG phonemization:

- https://github.com/OHF-Voice/piper1-gpl
- Install package: `pip install piper-tts` after selecting a supported Python environment and voice.
- Standard public voices are trained for existing languages. Replacing input spelling with Neva IPA **does not guarantee** perfect `θ ð ʃ y` or stress; a voice model must support the phonemes and be appropriately trained.
- For higher accuracy, train or adapt a model with recorded Neva utterances and their phoneme transcriptions; evaluate pronunciation by listening and maintaining a corpus of expected readings.
- Piper engine licensing is GPL-3.0; voice files may have additional/different licenses. Check distribution implications before bundling into a product.

On an Apple Silicon Mac, both eSpeak NG and local inference are practical places to experiment, but avoid committing downloaded model weights, large checkpoints or recordings to Git.

## Stage 4 — end-to-end text tools

The project's first interpreter should be **morphology and dictionary driven**:

1. Store source-of-truth lexemes (headword, gender, stem, root reference, source confidence).
2. Generate valid declensions and verb forms programmatically.
3. Build a small parser for a defined subset of simple Neva sentences.
4. Only then build English → Neva translation with a restricted syntax and an explicit 'unknown/ambiguous' response.
5. Add the TTS engine behind a single interface such as `speak(text: str) -> bytes` and integration tests.

Do not represent dictionary lookup or a few hand-written sentence templates as an accurate general translator. Constructed-language translation needs a robust grammar and a sufficiently large lexicon.

## Immediate local commands

```sh
python3 scripts/neva.py lookup water
python3 scripts/neva.py decline vulkos M --case accusative --number plural
python3 scripts/neva.py conjugate beren --tense past
python3 scripts/neva.py ipa "Kapo beroto vodrom."
python3 -m unittest discover -s tests -v
```
