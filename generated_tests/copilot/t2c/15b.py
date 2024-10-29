import unittest

def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    """
    if n < 0:
        return ''
    return ' '.join(map(str, range(n + 1)))

class TestStringSequenceFunction(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
    
    def test_zero_case(self):
        self.assertEqual(string_sequence(0), '0')
    
    def test_positive_integer(self):
        self.assertEqual(string_sequence(3), '0 1 2 3')
    
    def test_negative_integer(self):
        self.assertEqual(string_sequence(-1), '')

if __name__ == '__main__':
    unittest.main()