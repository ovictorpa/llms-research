import unittest

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

class TestCountDistinctCharacters(unittest.TestCase):
    def test_count_distinct_characters(self):
        # Test case 1: Empty string
        self.assertEqual(count_distinct_characters(""), 0)

        # Test case 2: Single character string
        self.assertEqual(count_distinct_characters("a"), 1)

        # Test case 3: String with repeated characters
        self.assertEqual(count_distinct_characters("hello"), 4)

        # Test case 4: String with mixed case
        self.assertEqual(count_distinct_characters("HeLlO"), 4)

        # Test case 5: String with spaces and punctuation
        self.assertEqual(count_distinct_characters("Hello, World!"), 8)

        # Test case 6: String with unicode characters
        self.assertEqual(count_distinct_characters("你好世界"), 4)

        # Test case 7: String with all distinct characters
        self.assertEqual(count_distinct_characters("abcdefg"), 7)

if __name__ == '__main__':
    unittest.main()
