import unittest

class TestSortNumbers(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_single_number(self):
        self.assertEqual(sort_numbers('one'), 'one')

    def test_multiple_numbers(self):
        self.assertEqual(sort_numbers('one three five'), 'one three five')

    def test_reversed_order(self):
        self.assertEqual(sort_numbers('nine seven eight six five four three two one zero'),
                     'zero one two three four five six seven eight nine')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_numbers('a b c d e f g h i j k l m n o p q r s t u v w x y z ')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            sort_numbers(123)

if __name__ == '__main__':
    unittest.main()