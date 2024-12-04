import unittest
from your_module import encrypt  # Replace with the actual module name

class TestEncrypt(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(encrypt("hello"), "lopxq")

    def test_uppercase(self):
        self.assertEqual(encrypt("HELLO"), "KHOOR")

    def test_mixed_case(self):
        self.assertEqual(encrypt("HeLlO"), "KhOpQ")

    def test_spaces(self):
        self.assertEqual(encrypt("hello world"), "lopxq wrold")

    def test_punctuation(self):
        self.assertEqual(encrypt("hello!"), "lopxq!")

    def test_numbers(self):
        self.assertEqual(encrypt("123"), "123")  # Numbers remain unchanged

    def test_non_alpha_chars(self):
        self.assertEqual(encrypt("hello$world"), "lopxq$wrold")

if __name__ == '__main__':
    unittest.main()