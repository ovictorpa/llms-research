import unittest
from typing import List

def parse_music(music_string: str) -> List[int]:

    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        # Test case 1: Empty string
        self.assertEqual(parse_music(""), [])

        # Test case 2: Single note
        self.assertEqual(parse_music("o"), [4])
        self.assertEqual(parse_music("o|"), [2])
        self.assertEqual(parse_music(".|"), [1])

        # Test case 3: Multiple notes
        self.assertEqual(parse_music("o o| .|"), [4, 4, 2, 1])

        # Test case 4: Spaces between notes
        self.assertEqual(parse_music("o o| .|"), [4, 4, 2, 1])

        # Test case 5: Extra spaces
        self.assertEqual(parse_music("  o   o|   .|  "), [4, 4, 2, 1])

        # Test case 6: Invalid notes
        self.assertEqual(parse_music("x y z"), [])

        # Test case 7: Mixed valid and invalid notes
        self.assertEqual(parse_music("o x o| y .|"), [4, 4, 2, 1])

if __name__ == '__main__':
    unittest.main()
