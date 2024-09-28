import unittest
from c2c.50a import encode_shift, decode_shift  # Adjust the import statement as needed

class TestShiftCipher(unittest.TestCase):

    def test_encode_basic(self):
        self.assertEqual(encode_shift("abc"), "fgh")

    def test_decode_basic(self):
        self.assertEqual(decode_shift("fgh"), "abc")

    def test_encode_wrap_around(self):
        self.assertEqual(encode_shift("xyz"), "cde")

    def test_decode_wrap_around(self):
        self.assertEqual(decode_shift("cde"), "xyz")

    def test_encode_empty_string(self):
        self.assertEqual(encode_shift(""), "")

    def test_decode_empty_string(self):
        self.assertEqual(decode_shift(""), "")

    def test_encode_single_character(self):
        sel
    def test_decode_single_character(self):
        self.assertEqual(decode_shift("f"), "a")

    def test_encode_long_string(self):
        self.assertEqual(encode_shift("abcdefghijklmnopqrstuvwxyz"), "fghijklmnopqrstuvwxyzabcde")

    def test_decode_long_string(self):
        self.assertEqual(decode_shift("fghijklmnopqrstuvwxyzabcde"), "abcdefghijklmnopqrstuvwxyz")

    def test_encode_with_spaces(self):
        self.assertEqual(encode_shift("abc def"), "fgh ijk")

    def test_decode_with_spaces(self):
        self.assertEqual(decode_shift("fgh ijk"), "abc def")

    def test_encode_decode_roundtrip(self):
        original = "hello world"
        encoded = encode_shift(original)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, original)

    def test_encode_non_lowercase(self):
        with self.assertRaises(ValueError):
            encode_shift("ABC")

    def test_decode_non_lowercase(self):
        with self.assertRaises(ValueError):
            decode_shift("ABC")

if __name__ == '__main__':
    unittest.main()
