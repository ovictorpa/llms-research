import unittest
from c2c.40a import triples_sum_to_zero  # Adjust the import statement as needed

class TestTriplesSumToZero(unittest.TestCase):

    def test_basic_true(self):
        self.assertTrue(triples_sum_to_zero([1, 3, 5, 0, -1, -5]))

    def test_basic_false(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0, -1, -4]))

    def test_all_zeros(self):
        self.assertTrue(triples_sum_to_zero([0, 0, 0]))

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

    def test_single_element(self):
        self.assertFalse(triples_sum_to_zero([0]))

    def test_two_elements(self):
        self.assertFalse(triples_sum_to_zero([0, 0]))

    def test_negative_numbers(self):
        self
    def test_all_positive(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4, 5]))

    def test_all_negative(self):
        self.assertFalse(triples_sum_to_zero([-1, -2, -3, -4, -5]))

    def test_large_numbers(self):
        self.assertTrue(triples_sum_to_zero([1000000, -500000, -500000, 200000, 300000, -1000000]))

    def test_duplicate_numbers(self):
        self.assertTrue(triples_sum_to_zero([1, 1, -2, 3, 4, -2]))

    def test_multiple_triples(self):
        self.assertTrue(triples_sum_to_zero([1, -1, 0, 2, -2, 0, 3, -3, 0]))

    def test_edge_case_large_list(self):
        large_list = list(range(-1000, 1001))  # -1000 to 1000
        self.assertTrue(triples_sum_to_zero(large_list))

if __name__ == '__main__':
    unittest.main()
