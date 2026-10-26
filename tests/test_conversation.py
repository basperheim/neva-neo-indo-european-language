"""Approved grammar milestones and a few practical conversations/stories."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import neva
from neva_comparison import inflect_adjective
from neva_relatives import decline_relative, matching_cases, PARADIGMS
from neva_translate import translate, TranslationError


class NewGrammarTests(unittest.TestCase):
    def test_relative_paradigms(self):
        self.assertEqual(decline_relative("jos", "nominative", "singular"), "jos")
        self.assertEqual(decline_relative("josa", "accusative", "singular"), "josam")
        self.assertEqual(decline_relative("jod", "nominative", "plural"), "joda")
        self.assertEqual(decline_relative("josa", "dative", "plural"), "joses")
        self.assertEqual(matching_cases("jod", "N", "singular"),
                         {"nominative", "accusative"})
        self.assertEqual(set(PARADIGMS), {"M", "F", "N"})
        with self.assertRaises(ValueError):
            decline_relative("ja", "genitive", "singular")  # ja already = yes

    def test_regular_comparisons(self):
        self.assertEqual(inflect_adjective("mezos", "comparative"), "mezoteros")
        self.assertEqual(inflect_adjective("mezos", "comparative", gender="F"), "mezotera")
        self.assertEqual(inflect_adjective("mezos", "superlative", gender="N"), "mezistom")
        self.assertEqual(inflect_adjective("nevos", "comparative"), "nevoteros")
        self.assertEqual(inflect_adjective("gelos", "superlative"), "gelistos")
        self.assertEqual(
            inflect_adjective("mezos", "comparative", gender="F",
                              grammatical_case="dative", number="plural"),
            "mezoteres",
        )

    def test_grammar_headwords_registered(self):
        entries = neva.load_lexicon()
        self.assertEqual(len(entries), 812)
        self.assertEqual(len({row["Neva"] for row in entries}), 812)
        items = {row["Neva"]: row for row in entries}
        for word in ("jos", "josa", "jod"):
            self.assertEqual(items[word]["Part of speech"], "relative pronoun")
        self.assertEqual(items["kod"]["Part of speech"], "conjunction")
        self.assertEqual(items["jaba"]["English"].split(" ", 1)[0], "if")

    def test_conditionals_and_causes(self):
        cases = {
            "Jaba beres vodrom, vel kapo vodrom.":
                "If you carry water, I will have water.",
            "Bero vodrom kod mathera ne bereth vodrom.":
                "I carry water because the mother does not carry water.",
            "Kod mathera ne bereth vodrom, bero vodrom.":
                "Because the mother does not carry water, I carry water.",
        }
        for sentence, expected in cases.items():
            with self.subTest(sentence=sentence):
                self.assertEqual(translate(sentence), expected)

    def test_english_conditional_and_causal(self):
        cases = {
            "If you carry water, I will have water.":
                "Jaba ty beres vodrom, ego vel kapo vodrom.",
            "I carry water because the mother does not carry water.":
                "Ego bero vodrom kod mathera ne bereth vodrom.",
        }
        for sentence, expected in cases.items():
            with self.subTest(sentence=sentence):
                self.assertEqual(translate(sentence, "en", "neva"), expected)

    def test_relative_clauses(self):
        self.assertEqual(
            translate("Vido matheram josa bereth vodrom."),
            "I see a mother who carries water.",
        )
        self.assertEqual(
            translate("Vido vulkom jos videth matheram."),
            "I see a wolf that sees a mother.",
        )
        self.assertEqual(
            translate("I see a mother who carries water.", "en", "neva"),
            "Ego vido matheram josa bereth vodrom.",
        )

    def test_comparatives_in_short_sentences(self):
        self.assertEqual(
            translate("Shos vulkos est mezoteros."),
            "This wolf is bigger.",
        )
        self.assertEqual(
            translate("Shos vulkos est mezoteros apo som vulkom."),
            "This wolf is bigger than that wolf.",
        )
        self.assertEqual(
            translate("This wolf is bigger.", "en", "neva"),
            "Shos vulkos est mezoteros.",
        )
        self.assertEqual(
            translate("This wolf is bigger than that wolf.", "en", "neva"),
            "Shos vulkos est mezoteros apo som vulkom.",
        )

    def test_directions(self):
        self.assertEqual(
            translate("Io ad dhverom."),
            "I go toward the door.",
        )
        self.assertEqual(
            translate("I go toward the door.", "en", "neva"),
            "Ego io ad dhverom.",
        )
        self.assertEqual(translate("Ie ad dhverom!"), "Go to the door!")
        self.assertEqual(translate("Ie per dhverom!"), "Go through the door!")
        self.assertEqual(
            translate("Ku est domom?"), "Where is the house?"
        )
        self.assertEqual(
            translate("Where is the house?", "en", "neva"),
            "Ku est domom?",
        )

    def test_everyday_phrases(self):
        examples = {
            "Yes!": "Ja!",
            "No!": "Ne!",
            "Good night!": "Vesa nokta!",
            "How are you?": "Komo es?",
            "Where is the road?": "Ku est pontos?",
        }
        for english, expected in examples.items():
            with self.subTest(english=english):
                self.assertEqual(translate(english, "en", "neva"), expected)

    def test_explicit_rejection_of_nested_or_unknown(self):
        for sentence in (
            "Jaba beres vodrom, vel kapo vodrom kod mathera ne bereth vodrom.",
            "Bero vodrom kod mysterious thing.",
        ):
            with self.subTest(sentence=sentence):
                with self.assertRaises(TranslationError):
                    translate(sentence)

    def test_cli_commands(self):
        script = ROOT / "scripts" / "neva.py"
        for args, expected in [
            (["decline-relative", "josa", "--case", "dative"], "jose"),
            (["compare", "mezos", "--degree", "superlative"], "mezistos"),
            (["translate", "Jaba beres vodrom, vel kapo vodrom."],
             "If you carry water, I will have water."),
        ]:
            with self.subTest(args=args):
                run = subprocess.run(
                    [sys.executable, str(script), *args],
                    text=True, capture_output=True, check=False,
                )
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertEqual(run.stdout.strip(), expected)


if __name__ == "__main__":
    unittest.main()
