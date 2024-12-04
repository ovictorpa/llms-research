import unittest
from your_module import move_one_ball  # Replace with the actual module name

class TestMoveOneBall(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element_list(self):
        self.assertTrue(move_one_ball([5]))

    def test_multiple_elements_list(self):
        self.assertTrue(move_one_ball([3, 1, 2]))
        self.assertFalse(move_one_ball([3, 4, 1, 2]))

    def test_identical_elements_list(self):
        self.assertFalse(move_one_ball([3, 3]))  # Not sorted
        self.assertTrue(move_one_ball([3, 2, 3]))  # Can be sorted by moving one ball

if __name__ == '__main__':
    unittest.main()