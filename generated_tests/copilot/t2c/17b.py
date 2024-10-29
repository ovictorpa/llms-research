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
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[note] for note in music_string.split()]

class TestParseMusic(unittest.TestCase):
    def test_mixed_notes(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    
    def test_only_whole_notes(self):
        self.assertEqual(parse_music('o o o o'), [4, 4, 4, 4])
    
    def test_only_half_notes(self):
        self.assertEqual(parse_music('o| o| o| o|'), [2, 2, 2, 2])
    
    def test_only_quarter_notes(self):
        self.assertEqual(parse_music('.| .| .| .|'), [1, 1, 1, 1])
    
    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

if __name__ == '__main__':
    unittest.main()