import unittest

def string_sequence(n: int) -> str:
    return ' '.join(str(x) for x in range(n + 1))

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        # Test case 1: n = 0
        self.assertEqual(string_sequence(0), "0")
        
        # Test case 2: n = 1
        self.assertEqual(string_sequence(1), "0 1")
        
        # Test case 3: n = 5
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        
        # Test case 4: n = 10
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")
        
        # Test case 5: n = 20
        expected = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
        self.assertEqual(string_sequence(20), expected)

if __name__ == '__main__':
    unittest.main()
