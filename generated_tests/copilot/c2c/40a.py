import unittest
from c2c._40a import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4, 5]))

    def test_negative_numbers(self):
        self.assertFalse(triples_sum_to_zero([-1, -2, -3, -4, -5]))

    def test_mixed_numbers(self):
        self.assertTrue(triples_sum_to_zero([-1, 1, 0]))
        self.assertTrue(triples_sum_to_zero([-5, 2, 3]))
        self.assertFalse(triples_sum_to_zero([-5, 2, 4]))

    def test_single_number(self):
        self.assertFalse(triples_sum_to_zero([0]))
        self.assertFalse(triples_sum_to_zero([1]))
        self.assertFalse(triples_sum_to_zero([-1]))

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

    def test_even_length_list(self):
        self.assertTrue(triples_sum_to_zero([-1, 1, 2, -2]))
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4]))

    def test_odd_length_list(self):
        self.assertTrue(triples_sum_to_zero([-1, 1, 2, -2, 0]))
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()