import unittest
from your_module import encode_cyclic, decode_cyclic  # Replace with the actual module name

class TestCyclicEncoding(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(encode_cyclic(""), "")
        self.assertEqual(decode_cyclic(""), "")

    def test_single_character(self):
        self.assertEqual(encode_cyclic("a"), "a")
        self.assertEqual(decode_cyclic("a"), "a")

    def test_three_characters(self):
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(decode_cyclic("bca"), "abc")

    def test_long_string(self):
        self.assertEqual(encode_cyclic("abcdef"), "bcfaed")
        self.assertEqual(decode_cyclic("bcfaed"), "abcdef")

    def test_odd_length_string(self):
        self.assertEqual(encode_cyclic("abcd"), "bcad")
        self.assertEqual(decode_cyclic("bcad"), "abcd")

if __name__ == '__main__':
    unittest.main()