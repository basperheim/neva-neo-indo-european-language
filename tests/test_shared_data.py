"""Cross-language shared lexical inventory contracts."""
import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import neva
import neva_translate
import neva_phrases
from neva_data import lexical_data


class SharedDataTests(unittest.TestCase):
    def test_json_is_python_runtime_source(self):
        data = lexical_data()
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(neva.STRONG_PAST, data["strong_past"])
        self.assertEqual(neva_translate.ENGLISH_NOUNS, data["english_nouns"])
        self.assertEqual(neva_translate.PREPOSITIONS, data["prepositions"])
        self.assertEqual(neva_translate.MASS_NOUNS, set(data["mass_nouns"]))
        self.assertEqual(data["english_nouns"]["meat"], "memsom")
        self.assertIn("meat", data["mass_nouns"])
        self.assertEqual(neva_phrases._PHRASES, data["phrases"]["en_to_neva"])
        self.assertEqual(neva_phrases._NEVA_TO_ENGLISH, data["phrases"]["neva_to_en"])
        for word, verb in data["verbs"].items():
            self.assertEqual(
                neva_translate.VERBS[word],
                (verb["base"], verb["third"], verb["past"], verb["participle"]),
            )

    def test_shared_headwords_exist_with_approved_part_of_speech(self):
        rows = {row["Neva"]: row for row in neva.load_lexicon()}
        data = lexical_data()
        for word in data["english_nouns"].values():
            self.assertEqual(rows[word]["Part of speech"], "noun", word)
        for word in data["verbs"]:
            self.assertEqual(rows[word]["Part of speech"], "verb", word)
        for word in data["english_adjectives"].values():
            self.assertEqual(rows[word]["Part of speech"], "adjective", word)
        for word in data["prepositions"]:
            self.assertEqual(rows[word]["Part of speech"], "preposition", word)
        for word in data["strong_past"]:
            self.assertEqual(rows[word]["Part of speech"], "verb", word)

    def test_reference_behavior_is_unchanged(self):
        from neva_translate import translate
        self.assertEqual(translate("I carry water.", source="en", target="neva"), "Ego bero vodrom.")
        self.assertEqual(translate("Mathera videth vulkom."), "The mother sees a wolf.")
        self.assertEqual(translate("Hello!", source="en", target="neva"), "Vese!")
        self.assertEqual(neva.STRONG_PAST["beren"], "bor")


if __name__ == "__main__":
    unittest.main()
