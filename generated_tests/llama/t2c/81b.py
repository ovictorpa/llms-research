import unittest

class TestNumericalLetterGrade(unittest.TestCase):

    def test_numerical_letter_grade_1(self):
        grades = [4.0, 3, 1.7, 2, 3.5]
        self.assertEqual(numerical_letter_grade(grades), ['A+', 'B', 'C-', 'C', 'A-'])

    def test_numerical_letter_grade_2(self):
        grades = [4.1, 3.8, 1.9, 2.1, 3.6]
        self.assertEqual(numerical_letter_grade(grades), ['A+', 'A', 'B-', 'C+', 'A-'])

    def test_numerical_letter_grade_3(self):
        grades = [4.0, 3.5, 1.8, 2.9, 3.8]
        self.assertEqual(numerical_letter_grade(grades), ['A+', 'B+', 'C', 'A-', 'A'])

    def test_numerical_letter_grade_4(self):
        grades = [0.1, -0.1, 4.5, 2.9, 3.8]
        self.assertEqual(numerical_letter_grade(grades), ['E', 'E', 'A+', 'A-', 'A'])

if __name__ == '__main__':
    unittest.main()