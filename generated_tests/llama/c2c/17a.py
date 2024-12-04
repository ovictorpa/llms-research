import unittest
from your_module import parse_music  # Replace with the actual module name

class TestParseMusic(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_music(""), [])

    def test_single_note(self):
        self.assertEqual(parse_music("o"), [4])

    def test_multiple_notes(self):
        self.assertEqual(parse_music("o o| .|."), [4, 2, 1])

    def test_invalid_note(self):
        self.assertRaises(KeyError, parse_music, "x")

    def test_empty_spaces(self):
        self.assertEqual(parse_music("   "), [])

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(parse_music(" o| .|."), [2, 1])

if __name__ == '__main__':
    unittest.main()