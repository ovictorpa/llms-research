import unittest
from c2c.17a import parse_music

class TestParseMusic(unittest.TestCase):

    def test_single_note(self):
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_multiple_notes(self):
        self.assertEqual(parse_music('o o| .|'), [4, 2, 1])
        self.assertEqual(parse_music('o| o .| o'), [2, 4, 1, 4])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_string_with_spaces(self):
        self.assertEqual(parse_music('  o  o|  .|  '), [4, 2, 1])
        self.assertEqual(parse_music('o|   o .|'), [2, 4, 1])

    def test_invalid_notes(self):
        self.assertEqual(parse_music('x y z'), [])

if __name__ == '__main__':
    unittest.main()