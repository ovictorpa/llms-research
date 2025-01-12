import unittest

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(encode_shift('xyz'), 'abc')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('fgh'), 'abc')
        self.assertEqual(decode_shift('abc'), 'xyz')

    def test_encode_shift_multiple_characters(self):
        self.assertEqual(encode_shift('abcdefg'), 'ijklmnop')
        self.assertEqual(encode_shift('abcdefghi'), 'jklmnopqrst')

    def test_decode_shift_all_chars_encoded(self):
        encoded = encode_shift('abcdefghijklmnopqrstuvwxyz')
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, 'abcdefghijklmnopqrstuvwxyz')

    def test_encode_shift_empty_string(self):
        self.assertEqual(encode_shift(''), '')

    def test_decode_shift_empty_string(self):
        self.assertEqual(decode_shift(''), '')

if __name__ == '__main__':
    unittest.main()