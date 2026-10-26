"""Lexicon expansion and faithful high-frequency coverage checks."""
import csv
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import neva
from neva_translate import translate, TranslationError


class VocabularyExpansionTests(unittest.TestCase):
    def test_core_new_nouns(self):
        entries = neva.load_lexicon()
        self.assertEqual(len(entries), 828)
        by_word = {r["Neva"]: r for r in entries}
        self.assertEqual(by_word["denegva"]["Gender"], "F")
        self.assertEqual(by_word["denegva"]["English"], "tongue, language")
        self.assertEqual(by_word["menos"]["Gender"], "M")
        self.assertIn("month", by_word["menos"]["English"])
        self.assertEqual(neva.decline("denegva", "F", "dative", "singular"), "denegve")
        self.assertEqual(neva.decline("ovisa", "F", "accusative"), "ovisam")
        self.assertEqual(neva.decline("sedotrom", "N", "nominative", "plural"),
                         "sedotra")
        for term in ("ovisa", "gansa", "musos", "susos", "kapros", "artos",
                     "miava", "sedotrom", "svepotrom", "dhotrom", "avosa",
                     "vesperos", "nu", "nudein", "septemodeinom", "zeninos"):
            with self.subTest(term=term):
                self.assertIn(term, by_word)
                self.assertTrue(by_word[term]["Notes"])
        self.assertEqual(by_word["miava"]["Historical status"], "Neva coinage")

    def test_single_word_translation_both_directions(self):
        cases = {
            "language": "denegva",
            "tongue": "denegva",
            "speech": "vekom",
            "word": "verdom",
            "sheep": "ovisa",
            "goose": "gansa",
            "cat": "miava",
            "chair": "sedotrom",
            "bed": "svepotrom",
            "table": "dhotrom",
            "knife": "kertotrom",
            "hammer": "plakotrom",
            "cup": "piotrom",
            "pot": "pekotrom",
            "bucket": "vodrokapotrom",
            "today": "nudein",
            "now": "nu",
            "week": "septemodeinom",
            "wise": "zeninos",
        }
        for english, word in cases.items():
            with self.subTest(english=english):
                self.assertEqual(
                    translate(english, source="en", target="neva"), word
                )
        self.assertEqual(translate("denegva"), "tongue / language")
        self.assertEqual(translate("Language", "en", "neva"), "Denegva")
        self.assertEqual(translate("veken"), "to speak")
        self.assertEqual(translate("I", "en", "neva"), "Ego")

    def test_ambiguity_and_zero_article_are_not_guessed(self):
        with self.assertRaises(TranslationError):
            translate("bear", "en", "neva")  # noun bear / verb bear
        with self.assertRaises(TranslationError):
            translate("the", "en", "neva")  # no obligatory article

    def test_ranked_frequency_coverage_has_100_rows(self):
        with (ROOT / "data" / "english_top100_coverage.tsv").open(
            encoding="utf-8", newline=""
        ) as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        self.assertEqual(len(rows), 100)
        self.assertEqual([int(row["Rank"]) for row in rows], list(range(1, 101)))
        self.assertEqual(len({row["English"] for row in rows}), 100)
        kinds = {row["Status"] for row in rows}
        self.assertEqual(kinds, {"lemma", "grammar", "partial", "gap"})
        headwords = {row["Neva"] for row in neva.load_lexicon()}
        for row in rows:
            with self.subTest(rank=row["Rank"], word=row["English"]):
                self.assertTrue(row["Notes"])
                self.assertTrue(row["Neva expression"])
                if row["Status"] == "lemma":
                    self.assertIn(row["Neva expression"], headwords)

    def test_cli_standalone_word_and_uncertain_article(self):
        script = ROOT / "scripts" / "neva.py"
        for args, expected in (
            (["translate", "--from", "en", "--to", "neva", "language"],
             "denegva\n"),
            (["translate", "denegva"], "tongue / language\n"),
            (["translate", "--from", "en", "--to", "neva", "sheep"],
             "ovisa\n"),
        ):
            with self.subTest(args=args):
                result = subprocess.run([sys.executable, str(script), *args],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)
        strict = subprocess.run(
            [sys.executable, str(script), "translate", "--strict",
             "--from", "en", "--to", "neva", "the"],
            capture_output=True, text=True,
        )
        self.assertEqual(strict.returncode, 2)
        self.assertIn("Translation unavailable:", strict.stderr)


if __name__ == "__main__":
    unittest.main()
