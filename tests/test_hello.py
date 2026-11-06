import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import bonjour  # noqa: E402


class TestBonjour(unittest.TestCase):
    def test_bonjour_defaut(self):
        self.assertEqual(bonjour(), "Bonjour monde !")

    def test_bonjour_nom(self):
        self.assertEqual(bonjour("Scotty"), "Bonjour Scotty !")


if __name__ == "__main__":
    unittest.main()
