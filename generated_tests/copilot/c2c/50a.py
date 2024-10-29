import unittest
from c2c._50a import encode_shift

class TestEncodeShift(unittest.TestCase):
    def test_encode_shift_with_lowercase(self):
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(encode_shift("xyz"), "cde")
        self.assertEqual(encode_shift("hello"), "mjqqt")

    def test_encode_shift_with_empty_string(self):
        self.assertEqual(encode_shift(""), "")

    def test_encode_shift_with_repeated_characters(self):
        self.assertEqual(encode_shift("aaa"), "fff")
        self.assertEqual(encode_shift("zzz"), "eee")

    def test_encode_shift_with_full_alphabet(self):
        self.assertEqual(encode_shift("abcdefghijklmnopqrstuvwxyz"), "fghijklmnopqrstuvwxyzabcde")

if __name__ == '__main__':
    unittest.main()