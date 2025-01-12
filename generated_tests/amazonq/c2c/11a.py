import unittest

class TestStringXOR(unittest.TestCase):
    def test_string_xor(self):
        # Test case 1: Equal length strings
        self.assertEqual(string_xor("1010", "0011"), "1001")
        
        # Test case 2: Unequal length strings
        self.assertEqual(string_xor("10", "0011"), "1001")
        
        # Test case 3: Empty strings
        self.assertEqual(string_xor("", ""), "")
        
        # Test case 4: Single character strings
        self.assertEqual(string_xor("1", "0"), "1")
        
        # Test case 5: Longer strings
        self.assertEqual(string_xor("101010101010", "010101010101"), "111111111111")

if __name__ == '__main__':
    unittest.main()
