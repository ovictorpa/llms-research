import unittest

def string_xor(a: str, b: str) -> str:
    """
    Perform a binary XOR operation on two strings consisting only of 1s and 0s.
    The result is returned as a string of 1s and 0s.
    
    >>> string_xor('010', '110')
    '100'
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestStringXOR(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_single_bit_strings(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('1', '1'), '0')

    def test_unequal_lengths(self):
        self.assertEqual(string_xor('010', '11'), '101')
        self.assertEqual(string_xor('1010', '111'), '1101')

    def test_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_mixed_cases(self):
        self.assertEqual(string_xor('01010101', '10101010'), '11111111')
        self.assertEqual(string_xor('101010101010', '010101010101'), '111111111111')

    def test_large_inputs(self):
        a = '0' * 1000000
        b = '1' * 1000000
        expected = '1' * 1000000
        self.assertEqual(string_xor(a, b), expected)

    def test_non_binary_input(self):
        with self.assertRaises(ValueError):
            string_xor('01a2', '1010')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_xor(123, '1010')

if __name__ == '__main__':
    unittest.main()
