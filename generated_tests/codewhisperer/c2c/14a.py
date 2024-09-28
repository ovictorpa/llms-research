import unittest
from typing import List

def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes(self):
        # Test case 1: Empty string
        self.assertEqual(all_prefixes(""), [])

        # Test case 2: Single character string
        self.assertEqual(all_prefixes("a"), ["", "a"])

        # Test case 3: Normal string
        self.assertEqual(all_prefixes("abc"), ["", "a", "ab", "abc"])

        # Test case 4: Longer string
        self.assertEqual(all_prefixes("hello"), ["", "h", "he", "hel", "hell", "hello"])

        # Test case 5: String with spaces
        self.assertEqual(all_prefixes("hello world"), ["", "h", "he", "hel", "hell", "hello", "hello ", "hello w", "hello wo", "hello wor", "hello worl", "hello world"])

        # Test case 6: Unicode string
        self.assertEqual(all_prefixes("你好世界"), ["", "你", "你好", "你好世", "你好世界"])

if __name__ == '__main__':
    unittest.main()
