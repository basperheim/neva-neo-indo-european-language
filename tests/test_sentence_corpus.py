"""Every published learner sentence must translate from Neva to English."""
import csv
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from neva_translate import translate


class BeginnerCorpusTests(unittest.TestCase):
    def test_curated_learner_corpus(self):
        with (ROOT / "data" / "sentence_corpus.tsv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        self.assertGreaterEqual(len(rows), 25)
        self.assertEqual(len({row["Neva"] for row in rows}), len(rows))
        for row in rows:
            with self.subTest(category=row["Category"], source=row["Neva"]):
                self.assertEqual(translate(row["Neva"]), row["English"])

    def test_examples_cli(self):
        script = ROOT / "scripts" / "neva.py"
        run = subprocess.run(
            [sys.executable, str(script), "examples", "--category", "Story",
             "--limit", "2"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(len(run.stdout.strip().splitlines()), 2)
        self.assertIn("[Story]", run.stdout)
        run = subprocess.run(
            [sys.executable, str(script), "examples", "--category", "Greeting",
             "--reverse", "--limit", "1"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("Hello!  —  Vese!", run.stdout)

    def test_translate_story_file(self):
        script = ROOT / "scripts" / "neva.py"
        story = ROOT / "examples" / "wolf_and_horse.neva"
        with (ROOT / "data" / "sentence_corpus.tsv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        translation = {row["Neva"]: row["English"] for row in rows}
        expected = [translation[line] for line in story.read_text(encoding="utf-8").splitlines()]
        run = subprocess.run(
            [sys.executable, str(script), "translate", "--file", str(story), "--strict"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(run.stdout.splitlines(), expected)

    def test_examples_do_not_claim_full_round_trip(self):
        # Forward corpus guarantee does not imply arbitrary English text is
        # reversible: English articles, context and case are often ambiguous.
        self.assertEqual(translate("Vulkos videth eshvom."), "The wolf sees a horse.")


if __name__ == "__main__":
    unittest.main()
