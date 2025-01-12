import unittest
from c2c.38a import encode_cyclic, decode_cyclic  # Adjust the import statement as needed

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_basic(self):
        self.assertEqual(encode_cyclic("abc"), "bca")

    def test_encode_longer_string(self):
        self.assertEqual(encode_cyclic("abcdef"), "bcadef")

    def test_encode_with_spaces(self):
        self.assertEqual(encode_cyclic("abc def"), "bca def")

    def test_encode_odd_length(self):
        self.assertEqual(encode_cyclic("abcde"), "bcade")

    def test_encode_empty_string(self):
        self.assertEqual(encode_cyclic(""), "")

    def test_encode_single_char(self):
        self.assertEqual(encode_cyclic("a"), "a")

    def test_encode_two_chars(self):
        self.assertEqual(encode_cyclic("ab"), "ba")

    def test_decode_basic(self):
        self.assertEqual(decode_cyclic("bca"), "abc")

    def test_decode_longer_string(self):
        self.assertEqual(decode_cyclic("bcadef"), "abcdef")

    def test_decode_with_spaces(self):
        self.assertEqual(decode_cyclic("bca def"), "abc def")

    def test_decode_odd_length(self):
        self.assertEqual(decode_cyclic("bcade"), "abcde")

    def test_decode_empty_string(self):
        self.assertEqual(decode_cyclic(""), "")

    def test_decode_single_char(self):
        self.assertEqual(decode_cyclic("a"), "a")

    def test_decode_two_chars(self):
        self.assertEqual(decode_cyclic("ba"), "ab")

    def test_encode_decode_roundtrip(self):
        original = "hello world"
        encoded = encode_cyclic(original)
        decoded = decode_cyclic(encoded)
        self.assertEqual(decoded, original)

    def test_decode_encode_roundtrip(self):
        original = "python programming"
        decoded = decode_cyclic(original)
        encoded = encode_cyclic(decoded)
        self.assertEqual(encoded, original)

if __name__ == '__main__':
    unittest.main()
