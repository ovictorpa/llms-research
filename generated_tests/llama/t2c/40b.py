import unittest

class TestTriplesSumToZero(unittest.TestCase):

    def test_no_triplets(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5]))
        self.assertFalse(triples_sum_to_zero([1, 2, 4]))

    def test_single_triplet(self):
        self.assertTrue(triples_sum_to_zero([-1, 0, 1]))
        self.assertTrue(triples_sum_to_zero([-1, -1, 2]))
        self.assertTrue(triples_sum_to_zero([1, -1, -1]))

    def test_multiple_triplets(self):
        self.assertTrue(triples_sum_to_zero([-3, 0, 3]))
        self.assertTrue(triples_sum_to_zero([-5, 0, 5]))
        self.assertTrue(triples_sum_to_zero([2, -4, 6]))

    def test_single_element_list(self):
        self.assertFalse(triples_sum_to_zero([1]))

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

if __name__ == '__main__':
    unittest.main()