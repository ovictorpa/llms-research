import unittest

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    words = numbers.split()
    sorted_words = sorted(words, key=lambda word: num_map[word])
    return ' '.join(sorted_words)

class TestSortNumbers(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
    
    def test_already_sorted(self):
        self.assertEqual(sort_numbers('one three five'), 'one three five')
    
    def test_reverse_sorted(self):
        self.assertEqual(sort_numbers('five three one'), 'one three five')
    
    def test_duplicate_numbers(self):
        self.assertEqual(sort_numbers('one one two two'), 'one one two two')
    
    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

if __name__ == '__main__':
    unittest.main()