import unittest
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format and return a list of integers
    corresponding to how many beats each note lasts.
    
    Legend:
    - 'o'  - whole note, lasts four beats
    - 'o|' - half note, lasts two beats
    - '.|' - quarter note, lasts one beat
    
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestParseMusicString(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_single_note(self):
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_invalid_note(self):
        with self.assertRaises(ValueError):
            parse_music('x')

    def test_mixed_notes(self):
        self.assertEqual(parse_music('o o| .| o| .|'), [4, 2, 1, 2, 1])
        self.assertEqual(parse_music('o| .| o .| o|'), [2, 1, 4, 1, 2])

    def test_consecutive_notes(self):
        self.assertEqual(parse_music('oooo'), [4, 4, 4, 4])
        self.assertEqual(parse_music('o|o|o|o|'), [2, 2, 2, 2])
        self.assertEqual(parse_music('.|.|.|.|'), [1, 1, 1, 1])

    def test_long_sequence(self):
        long_sequence = 'o|' * 1000 + '.|' * 1000
        expected_output = [2] * 1000 + [1] * 1000
        self.assertEqual(parse_music(long_sequence), expected_output)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            parse_music(123)

if __name__ == '__main__':
    unittest.main()
