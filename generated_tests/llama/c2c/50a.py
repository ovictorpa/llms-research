import unittest

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift_with_lowercase(self):
        # Test with lowercase letters
        self.assertEqual(encode_shift("hello"), "mjqqt")

    def test_encode_shift_with_uppercase(self):
        # Test with uppercase letters
        self.assertEqual(encode_shift("HELLO"), "MQJQW")

    def test_decode_shift_with_lowercase(self):
        # Test with lowercase letters after encoding
        self.assertEqual(decode_shift(encode_shift("hello")), "hello")

    def test_decode_shift_with_uppercase(self):
        # Test with uppercase letters after encoding
        self.assertEqual(decode_shift(encode_shift("HELLO")), "HELLO")

    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(decode_shift(""), "")

    def test_non_alphabetical_characters(self):
        # Test with non-alphabetical characters
        self.assertEqual(encode_shift("hello world!"), "mjqqt xpsme!")

    def test_input_not_string(self):
        # Test with input not a string
        with self.assertRaises(TypeError):
            encode_shift(123)

if __name__ == '__main__':
    unittest.main()