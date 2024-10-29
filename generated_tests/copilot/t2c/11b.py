# t2c/test_11b.txt
import unittest
from your_module import string_xor  # Replace 'your_module' with the actual module name

class TestStringXor(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(string_xor('010', '110'), '100')
    
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
    
    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            string_xor('01', '001')
    
    def test_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')
    
    def test_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

if __name__ == '__main__':
    unittest.main()