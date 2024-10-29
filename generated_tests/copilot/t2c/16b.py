import unittest
from your_module import count_distinct_characters  # Adjust the import as necessary

class TestCountDistinctCharacters(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    
    def test_all_same_characters(self):
        self.assertEqual(count_distinct_characters('aaaaa'), 1)
    
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)
    
    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$$%^'), 6)
    
    def test_numeric_characters(self):
        self.assertEqual(count_distinct_characters('123321'), 3)

if __name__ == '__main__':
    unittest.main()