import unittest
from your_module import sort_even  # Replace 'your_module' with the actual name of the module where the function

class TestSortEven(unittest.TestCase):

    def test_sort_even_1(self):
        l = [1, 2, 3]
        expected_result = [1, 2, 3]
        self.assertEqual(sort_even(l), expected_result)

    def test_sort_even_2(self):
        l = [5, 6, 3, 4]
        expected_result = [3, 6, 5, 4]
        self.assertEqual(sort_even(l), expected_result)

if __name__ == '__main__':
    unittest.main()