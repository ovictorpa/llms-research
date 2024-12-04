import unittest
from your_module import find_zero  # Replace 'your_module' with the actual name of the module where the function

class TestFindZero(unittest.TestCase):

    def test_find_zero_1(self):
        xs = [1, 2]
        expected_result = -0.5
        self.assertAlmostEqual(find_zero(xs), expected_result)

    def test_find_zero_2(self):
        xs = [-6, 11, -6, 1]
        expected_result = 1.0
        self.assertAlmostEqual(find_zero(xs), expected_result)

if __name__ == '__main__':
    unittest.main()