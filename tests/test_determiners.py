"""Approved determiner paradigms and CLI regression tests."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from neva_determiners import (  # noqa: E402
    CASES, HEADWORDS, PARADIGMS, decline_determiner, match_determiner,
    english_determiner,
)


class DeterminerTests(unittest.TestCase):
    def test_paradigms_all_have_four_cases_and_two_numbers(self):
        for meaning, genders in PARADIGMS.items():
            for gender in ("M", "F", "N"):
                for number in ("singular", "plural"):
                    with self.subTest(meaning=meaning, gender=gender, number=number):
                        self.assertEqual(set(genders[gender][number]), set(CASES))
                        self.assertTrue(all(genders[gender][number].values()))

    def test_expected_surface_forms(self):
        self.assertEqual(decline_determiner("shos", "nominative", "singular"), "shos")
        self.assertEqual(decline_determiner("shos", "accusative", "singular"), "shom")
        self.assertEqual(decline_determiner("sha", "dative", "singular"), "she")
        self.assertEqual(decline_determiner("shod", "nominative", "plural"), "sha")
        self.assertEqual(decline_determiner("so", "nominative", "plural"), "toi")
        self.assertEqual(decline_determiner("sa", "accusative", "singular"), "sam")
        self.assertEqual(decline_determiner("tod", "dative", "singular"), "toi")
        self.assertEqual(decline_determiner("kinos", "nominative", "plural"), "kines")
        self.assertEqual(decline_determiner("kina", "dative", "plural"), "kines")
        self.assertEqual(decline_determiner("kinom", "accusative", "plural"), "kina")

    def test_agreement_and_homographs(self):
        self.assertEqual(match_determiner("sha", "F", "singular", "nominative"), "this")
        self.assertEqual(match_determiner("sha", "N", "plural", "nominative"), "this")
        self.assertIsNone(match_determiner("sha", "M", "singular", "nominative"))
        self.assertEqual(match_determiner("kinom", "N", "singular", "accusative"), "which")
        self.assertEqual(english_determiner("this", "plural"), "these")
        self.assertEqual(english_determiner("that", "plural"), "those")
        self.assertEqual(english_determiner("which", "plural"), "which")

    def test_only_citation_forms_are_accepted(self):
        self.assertEqual(len(HEADWORDS), 9)
        with self.assertRaises(ValueError):
            decline_determiner("unknown", "dative", "singular")

    def test_cli(self):
        script = ROOT / "scripts" / "neva.py"
        for args, expected in [
            (["shos", "--case", "accusative"], "shom"),
            (["sha", "--case", "dative"], "she"),
            (["kinos", "--number", "plural"], "kines"),
        ]:
            with self.subTest(args=args):
                completed = subprocess.run(
                    [sys.executable, str(script), "decline-determiner", *args],
                    text=True, capture_output=True, check=False
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertEqual(completed.stdout.strip(), expected)


if __name__ == "__main__":
    unittest.main()
