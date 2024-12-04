import unittest
from your_module import find_closest_elements  # Replace with the actual module name

class TestFindClosestElements(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_closest_elements([1]), (1, 1))

    def test_two_elements(self):
        self.assertEqual(find_closest_elements([1, 2]), (1, 2))

    def test_three_elements(self):
        self.assertEqual(find_closest_elements([1, 2, 3]), (1, 2))

    def test_multiple_elements(self):
        self.assertEqual(find_closest_elements([1, 2, 4, 5]), (2, 3))

    def test_identical_elements(self):
        self.assertEqual(find_closest_elements([-1, -1, 0, 0, 1, 1]), (-1, -1))

if __name__ == '__main__':
    unittest.main()