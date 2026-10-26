"""Bounded translator contract: supported sentences work; unsupported ones fail loudly."""
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from neva_translate import TranslationError, translate


class TranslatorTests(unittest.TestCase):
    def test_neva_statements(self):
        examples = {
            "Bero vodrom.": "I carry water.",
            "Boro vodrom.": "I carried water.",
            "Kapo beroto vodrom.": "I have carried water.",
            "Mathera videth vulkom.": "The mother sees a wolf.",
            "Bero vodrom mathere.": "I carry water to the mother.",
            "Kapo gerbotrom ke menotrom.": "I have a pen and a computer.",
            "So est patheros.": "He is a father.",
            "Menotrom est nevom.": "The computer is new.",
            "Ty beres vodrom.": "You carry water.",
            "Vulkes vidont eshvons.": "The wolves see horses.",
            "Bere vodrom!": "Carry water!",
            "Vel bero vodrom.": "I will carry water.",
            "Ne bero vodrom.": "I do not carry water.",
            "Ka beres vodrom?": "Do you carry water?",
        }
        for source, expected in examples.items():
            with self.subTest(source=source):
                self.assertEqual(translate(source), expected)

    def test_english_statements(self):
        examples = {
            "I carry water.": "Ego bero vodrom.",
            "I carried water.": "Ego boro vodrom.",
            "I have carried water.": "Ego kapo beroto vodrom.",
            "The mother sees a wolf.": "Mathera videth vulkom.",
            "You carry water.": "Ty beres vodrom.",
            "I will carry water.": "Ego vel bero vodrom.",
            "She sees a new wolf.": "Sa videth nevom vulkom.",
            "I carry water to the mother.": "Ego bero vodrom mathere.",
        }
        for source, expected in examples.items():
            with self.subTest(source=source):
                self.assertEqual(
                    translate(source, source="en", target="neva"), expected
                )

    def test_cli_translate_command_and_flags(self):
        script = Path(__file__).resolve().parents[1] / "scripts" / "neva.py"
        cases = [
            (["translate", "Kapo beroto vodrom."], "I have carried water.\n"),
            (["translate", "--from", "neva", "--to", "en",
              "Bero vodrom mathere."], "I carry water to the mother.\n"),
            (["translate", "--from", "en", "--to", "neva",
              "I carry water."], "Ego bero vodrom.\n"),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                completed = subprocess.run(
                    [sys.executable, str(script), *args],
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertEqual(completed.stdout, expected)

    def test_cli_rejects_unsupported_input(self):
        script = Path(__file__).resolve().parents[1] / "scripts" / "neva.py"
        completed = subprocess.run(
            [sys.executable, str(script), "translate", "Some nonsense statement."],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("Translation unavailable:", completed.stderr)
        self.assertEqual(completed.stdout, "")

    def test_unsupported_input_is_explicit(self):
        invalid = [
            "This is a mysterious unknown sentence.",
            "Bero supercalifragilistic.",
            "Ka boro vodrom?",
            "Vulkos beres vodrom.",  # subject / verb agreement mismatch
        ]
        for sentence in invalid:
            with self.subTest(source=sentence), self.assertRaises(TranslationError):
                translate(sentence)
        with self.assertRaises(TranslationError):
            translate("I carry water.", source="fr", target="neva")


if __name__ == "__main__":
    unittest.main()
