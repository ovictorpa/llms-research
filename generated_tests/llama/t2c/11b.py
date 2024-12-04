import unittest
from your_module import string_xor  # Replace 'your_module' with the actual module name

class TestStringXor(unittest.TestCase):

    def test_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            string_xor('abc', 'def')

if __name__ == '__main__':
    unittest.main()