import unittest

def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    return ' '.join(sorted(numbers.split(), key=lambda x: value_map[x]))

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        # Test case 1: Empty string
        self.assertEqual(sort_numbers(""), "")

        # Test case 2: Single number word
        self.assertEqual(sort_numbers("two"), "two")

        # Test case 3: Multiple number words in sorted order
        self.assertEqual(sort_numbers("one two three"), "one two three")

        # Test case 4: Multiple number words in unsorted order
        self.assertEqual(sort_numbers("three two one"), "one two three")

        # Test case 5: Duplicate number words
        self.assertEqual(sort_numbers("one two one three"), "one one two three")

        # Test case 6: Mixed case
        self.assertEqual(sort_numbers("One Two Three"), "One Two Three")

        # Test case 7: Invalid words
        self.assertEqual(sort_numbers("one invalid two"), "one two")

        # Test case 8: Spaces between words
        self.assertEqual(sort_numbers("one   two   three"), "one two three")

        # Test case 9: Unicode characters
        self.assertEqual(sort_numbers("一 二 三"), "一 二 三")

if __name__ == '__main__':
    unittest.main()
