import unittest
from your_module import parse_music  # Replace 'your_module' with the actual module name
from typing import List

class TestParseMusic(unittest.TestCase):

    def test_simple_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            parse_music('')

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            parse_music('o! o| o.')

    def test_no_notes(self):
        self.assertEqual(parse_music('|'), [])

if __name__ == '__main__':
    unittest.main()