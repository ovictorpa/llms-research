import unittest
from your_module import string_xor  # Replace with the actual module name

class TestStringXOR(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor("", ""), "")

    def test_single_character_strings(self):
        self.assertEqual(string_xor("0", "1"), "1")
        self.assertEqual(string_xor("1", "0"), "1")

    def test_two_character_strings(self):
        self.assertEqual(string_xor("00", "11"), "00")
        self.assertEqual(string_xor("01", "10"), "01")
        self.assertEqual(string_xor("11", "00"), "11")
        self.assertEqual(string_xor("1010", "0101"), "1111")

    def test_long_strings(self):
        self.assertEqual(string_xor("01101001", "11010010"), "00111011")
        self.assertEqual(string_xor("10101010", "10101010"), "00000000")


if __name__ == '__main__':
    unittest.main()