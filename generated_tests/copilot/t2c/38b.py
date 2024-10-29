import unittest
from typing import List

def encode_cyclic(s: str) -> str:
    """
    Encodes the input string by cycling characters within each group of three.
    For each group of three characters, the function cycles the characters to the left.
    Groups with fewer than three characters remain unchanged.

    >>> encode_cyclic('abcdefg')
    'bca defg'
    >>> encode_cyclic('abcde')
    'bca de'
    """
    result = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            result.append(group[1:] + group[0])
        else:
            result.append(group)
    return ''.join(result)

def decode_cyclic(s: str) -> str:
    """
    Decodes a string that was encoded with the encode_cyclic function.
    Since encoding is a reversible operation, decoding is achieved by encoding the string twice.

    >>> decode_cyclic('bca defg')
    'abcdefg'
    >>> decode_cyclic('bca de')
    'abcde'
    """
    return encode_cyclic(encode_cyclic(s))

class TestCyclicEncoding(unittest.TestCase):
    def test_encode_example_1(self):
        self.assertEqual(encode_cyclic('abcdefg'), 'bca defg')
    
    def test_encode_example_2(self):
        self.assertEqual(encode_cyclic('abcde'), 'bca de')
    
    def test_encode_empty_string(self):
        self.assertEqual(encode_cyclic(''), '')
    
    def test_encode_single_character(self):
        self.assertEqual(encode_cyclic('a'), 'a')
    
    def test_encode_two_characters(self):
        self.assertEqual(encode_cyclic('ab'), 'ab')
    
    def test_decode_example_1(self):
        self.assertEqual(decode_cyclic('bca defg'), 'abcdefg')
    
    def test_decode_example_2(self):
        self.assertEqual(decode_cyclic('bca de'), 'abcde')
    
    def test_decode_empty_string(self):
        self.assertEqual(decode_cyclic(''), '')
    
    def test_decode_single_character(self):
        self.assertEqual(decode_cyclic('a'), 'a')
    
    def test_decode_two_characters(self):
        self.assertEqual(decode_cyclic('ab'), 'ab')

if __name__ == '__main__':
    unittest.main()