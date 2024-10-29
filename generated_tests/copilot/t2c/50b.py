import unittest

def encode_shift(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    >>> encode_shift('abc')
    'fgh'
    >>> encode_shift('xyz')
    'abc'
    """
    return ''.join(chr((ord(char) - ord('a') + 5) % 26 + ord('a')) for char in s)

def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with the encode_shift function.
    Returns the decoded string.

    >>> decode_shift('fgh')
    'abc'
    >>> decode_shift('abc')
    'xyz'
    """
    return ''.join(chr((ord(char) - ord('a') - 5) % 26 + ord('a')) for char in s)

class TestShiftEncoding(unittest.TestCase):
    def test_encode_example_1(self):
        self.assertEqual(encode_shift('abc'), 'fgh')
    
    def test_encode_example_2(self):
        self.assertEqual(encode_shift('xyz'), 'cde')
    
    def test_encode_empty_string(self):
        self.assertEqual(encode_shift(''), '')
    
    def test_encode_single_character(self):
        self.assertEqual(encode_shift('a'), 'f')
    
    def test_encode_wrap_around(self):
        self.assertEqual(encode_shift('wxyz'), 'bcde')
    
    def test_decode_example_1(self):
        self.assertEqual(decode_shift('fgh'), 'abc')
    
    def test_decode_example_2(self):
        self.assertEqual(decode_shift('cde'), 'xyz')
    
    def test_decode_empty_string(self):
        self.assertEqual(decode_shift(''), '')
    
    def test_decode_single_character(self):
        self.assertEqual(decode_shift('f'), 'a')
    
    def test_decode_wrap_around(self):
        self.assertEqual(decode_shift('bcde'), 'wxyz')

if __name__ == '__main__':
    unittest.main()