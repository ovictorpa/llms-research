import unittest
from c2c.109a import move_one_ball  # Adjust the import statement as needed

class TestMoveOneBall(unittest.TestCase):

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_one_move_needed(self):
        self.assertTrue(move_one_ball([2, 3, 4, 5, 1]))

    def test_no_move_possible(self):
        self.assertFalse(move_one_ball([5, 4, 3, 2, 1]))

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([1]))

    def test_two_elements_sorted(self):
        self.assertTrue(move_one_ball([1, 2]))

    def test_two_elements_unsorted(self):
        self.assertTrue(move_one_ball([2, 1]))

    def test_duplicate_elements(self):
        self.assertTrue(move_one_ball([1, 2, 2, 3, 3, 4]))

    def test_all_same_elements(self):
        self.assertTrue(move_one_ball([1, 1, 1, 1, 1]))

    def test_complex_case_true(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_complex_case_false(self):
        self.assertFalse(move_one_ball([3, 4, 1, 2, 5]))

    def test_negative_numbers(self):

    def test_mixed_positive_negative(self):
        self.assertTrue(move_one_ball([0, 1, 2, -2, -1]))

if __name__ == '__main__':
    unittest.main()
