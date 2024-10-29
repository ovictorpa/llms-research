import unittest
from c2c import 11a

class TestStringXor(unittest.TestCase):

    def test_equal_length_strings(self):
        self.assertEqual(11a.string_xor('1100', '1010'), '0110')
        self.assertEqual(11a.string_xor('1111', '0000'), '1111')
        self.assertEqual(11a.string_xor('0000', '0000'), '0000')

    def test_different_length_strings(self):
        self.assertEqual(11a.string_xor('110', '1010'), '011')
        self.assertEqual(11a.string_xor('1111', '00'), '110')
        self.assertEqual(11a.string_xor('0', '0000'), '0')

    def test_empty_strings(self):
        self.assertEqual(11a.string_xor('', ''), '')

    def test_single_character_strings(self):
        self.assertEqual(11a.string_xor('1', '0'), '1')
        self.assertEqual(11a.string_xor('0', '0'), '0')
        self.assertEqual(11a.string_xor('1', '1'), '0')

if __name__ == '__main__':
    unittest.main()