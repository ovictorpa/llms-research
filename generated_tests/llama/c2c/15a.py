import unittest

class TestStringSequenceFunction(unittest.TestCase):

    def test_positive_integer(self):
        # Test with a positive integer
        self.assertEqual(string_sequence(3), "1 2 3")

    def test_non_integer_input(self):
        # Test that type error is raised when input is not an integer
        with self.assertRaises(TypeError):
            string_sequence("a")

    def test_negative_integer_input(self):
        # Test that a TypeError is raised when input is negative
        with self.assertRaises(TypeError):
            string_sequence(-1)

    def test_zero_input(self):
        # Test that a TypeError is raised when input is zero
        with self.assertRaises(TypeError):
            string_sequence(0)

    def test_large_integer_input(self):
        # Test with a large positive integer
        result = string_sequence(100)
        expected = " ".join(str(x) for x in range(101))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()