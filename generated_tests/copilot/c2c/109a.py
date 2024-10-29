import unittest
from c2c._109a import move_one_ball

class TestMoveOneBall(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([1]))

    def test_sorted_list(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_rotated_sorted_list(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_unsorted_list(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_all_elements_same(self):
        self.assertTrue(move_one_ball([2, 2, 2, 2]))

    def test_two_elements_sorted(self):
        self.assertTrue(move_one_ball([1, 2]))

    def test_two_elements_unsorted(self):
        self.assertFalse(move_one_ball([2, 1]))

if __name__ == '__main__':
    unittest.main()