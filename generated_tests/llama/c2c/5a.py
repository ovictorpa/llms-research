import unittest
from your_module import intersperse  # Replace with the actual module name

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        input_numbers = []
        expected_output = []
        self.assertEqual(intersperse(input_numbers, 0), expected_output)

    def test_single_element_list(self):
        input_numbers = [1]
        expected_output = [1]
        self.assertEqual(intersperse(input_numbers, 0), expected_output)

    def test_two_elements(self):
        input_numbers = [1, 2]
        expected_output = [1, 0, 2]
        self.assertEqual(intersperse(input_numbers, 0), expected_output)

    def test_three_elements(self):
        input_numbers = [1, 2, 3]
        expected_output = [1, 0, 2, 0, 3]
        self.assertEqual(intersperse(input_numbers, 0), expected_output)

    def test_long_list(self):
        input_numbers = list(range(10))
        expected_output = [0] + list(map(str, range(10))) + [0]
        self.assertEqual(intersperse(input_numbers, 0), expected_output)

if __name__ == '__main__':
    unittest.main()