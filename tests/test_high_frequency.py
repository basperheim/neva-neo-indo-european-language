"""High-frequency English function-word semantics and bounded Neva modals."""
import csv
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import neva
from neva_comparison import inflect_adjective
from neva_translate import TranslationError, translate


class FrequencyGapTests(unittest.TestCase):
    def test_851_unique_headwords_and_unchanged_declensions(self):
        rows = neva.load_lexicon()
        self.assertEqual(len(rows), 851)
        self.assertEqual(len({x["Neva"] for x in rows}), 851)
        self.assertEqual(neva.decline("vulkos", "M", "nominative", "plural"), "vulkes")
        self.assertEqual(neva.decline("mathera", "F", "dative", "singular"), "mathere")
        self.assertEqual(neva.decline("denegva", "F", "accusative", "singular"), "denegvam")

    def test_frequency_audit_has_no_unsupported_unclassified_gaps(self):
        with (ROOT / "data" / "english_top100_coverage.tsv").open(
            encoding="utf-8", newline=""
        ) as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        self.assertEqual(len(rows), 100)
        counts = {k: sum(r["Status"] == k for r in rows) for k in ("lemma", "grammar", "partial", "gap")}
        self.assertEqual(counts, {"lemma": 57, "grammar": 25, "partial": 18, "gap": 0})
        for row in rows:
            self.assertTrue(row["Notes"])
            self.assertTrue(row["Neva expression"])

    def test_new_spatial_prepositions(self):
        self.assertEqual(translate("I carry water on the table.", "en", "neva"),
                         "Ego bero vodrom epi dhotrom.")
        self.assertEqual(translate("Bero vodrom epi dhotrom."),
                         "I carry water on the table.")
        self.assertEqual(translate("I go at the house.", "en", "neva"),
                         "Ego io api domom.")
        self.assertEqual(translate("Io api domom."), "I go at the home.")

    def test_some_and_other_agree_with_nouns(self):
        self.assertEqual(translate("I see some water.", "en", "neva"),
                         "Ego vido somom vodrom.")
        self.assertEqual(translate("Vido somom vodrom."), "I see some water.")
        self.assertEqual(translate("I see another wolf.", "en", "neva"),
                         "Ego vido alterom vulkom.")  # extend English lexical alias below

    def test_can_and_could_past_ability(self):
        sentences = [
            ("I can carry water.", "Ego mago beren vodrom."),
            ("You can carry water.", "Ty mages beren vodrom."),
            ("I could carry water.", "Ego emago beren vodrom."),
            ("She can see a wolf.", "Sa mageth viden vulkom."),
        ]
        for english, neva_text in sentences:
            with self.subTest(english=english):
                self.assertEqual(translate(english, "en", "neva"), neva_text)
                self.assertEqual(translate(neva_text), english)

    def test_would_hypothetical_result(self):
        self.assertEqual(translate("I would carry water.", "en", "neva"),
                         "Ego vela bero vodrom.")
        self.assertEqual(translate("Ego vela bero vodrom."), "I would carry water.")
        self.assertEqual(translate("She would see a wolf.", "en", "neva"),
                         "Sa vela videth vulkom.")
        self.assertEqual(translate("Sa vela videth vulkom."), "She would see a wolf.")
        with self.assertRaises(TranslationError):
            translate("I would have carried water.", "en", "neva")

    def test_like_and_use_as_finite_verbs(self):
        self.assertEqual(translate("I like water.", "en", "neva"),
                         "Ego lubo vodrom.")
        self.assertEqual(translate("Lubo vodrom."), "I like water.")
        self.assertEqual(translate("I use a pen.", "en", "neva"),
                         "Ego prodho gerbotrom.")
        self.assertEqual(translate("Prodho gerbotrom."), "I use a pen.")

    def test_non_gradable_quantifiers(self):
        self.assertEqual(inflect_adjective("somos", "positive", gender="F"), "soma")
        self.assertEqual(inflect_adjective("kvenos", "positive", gender="N"), "kvenom")
        with self.assertRaises(ValueError):
            inflect_adjective("solvos", "superlative")
        with self.assertRaises(ValueError):
            inflect_adjective("primos", "comparative")

    def test_no_unaddressed_top100_rows_cli(self):
        script = ROOT / "scripts" / "neva.py"
        completed = subprocess.run(
            [sys.executable, str(script), "coverage", "--status", "gap"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(
            completed.stdout.strip(),
            "No coverage entries with status 'gap'.",
        )

    def test_cli_reports_partial_senses_and_headwords(self):
        script = ROOT / "scripts" / "neva.py"
        runs = [
            (["coverage", "--status", "partial", "--limit", "2"], "partial"),
            (["translate", "--from", "en", "--to", "neva", "time"], "temom"),
            (["translate", "Ego mago beren vodrom."], "I can carry water."),
        ]
        for args, expected in runs:
            with self.subTest(args=args):
                completed = subprocess.run(
                    [sys.executable, str(script), *args],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertIn(expected, completed.stdout)


if __name__ == "__main__":
    unittest.main()
