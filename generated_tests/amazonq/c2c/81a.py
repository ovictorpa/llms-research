import unittest
from c2c.81a import numerical_letter_grade  # Adjust the import statement as needed

class TestNumericalLetterGrade(unittest.TestCase):

    def test_basic_grades(self):
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_edge_cases(self):
        grades = [4.0, 3.71, 3.69, 3.31, 3.29, 3.01, 2.99, 2.71, 2.69, 2.31, 2.29, 2.01, 1.99, 1.71, 1.69, 1.31, 1.29, 1.01, 0.99, 0.71, 0.69, 0.01]
        expected = ['A+', 'A', 'A-', 'A-', 'B+', 'B+', 'B', 'B', 'B-', 'B-', 'C+', 'C+', 'C', 'C', 'C-', 'C-', 'D+', 'D+', 'D', 'D', 'D-', 'D-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([3.5]), ['A-'])

    def test_repeated_grades(self):
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_out_of_range_high(self):
        self.assertEqual(numerical_letter_grade([5.0]), ['A+'])

    def test_out_of_range_low(self):
        self.assertEqual(numerical_letter_grade([-1.0]), ['E'])

    def test_mixed_grades(self):
        grades = [4.0, 3.5, 2.9, 1.8, 0.5]
        self.assertEqual(numerical_letter_grade(grades), expected)

if __name__ == '__main__':
    unittest.main()
