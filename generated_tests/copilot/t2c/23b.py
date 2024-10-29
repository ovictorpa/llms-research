import unittest

def strlen(string: str) -> int:
    """
    Return the length of the given string.
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)
    
    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)
    
    def test_single_character(self):
        self.assertEqual(strlen('a'), 1)
    
    def test_long_string(self):
        self.assertEqual(strlen('hello world'), 11)

if __name__ == '__main__':
    unittest.main()