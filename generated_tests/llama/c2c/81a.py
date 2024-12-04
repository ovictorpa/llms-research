import unittest
from your_module import numerical_letter_grade  # Replace with the actual module name

class TestLetterGrades(unittest.TestCase):
    def test_perfect_gpa(self):
        grades = [4.0]
        expected_output = ["A+"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_high_gpas(self):
        grades = [3.8, 3.9, 4.0]
        expected_output = ["A", "A", "A+"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_low_to_moderate_gpas(self):
        grades = [2.5, 2.6, 2.7]
        expected_output = ["C+", "B-", "B+"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_very_low_gpas(self):
        grades = [0.8, 1.0]
        expected_output = ["D", "E"]
        self.assertEqual(numerical_letter_grade(grades), expected_output)

if __name__ == '__main__':
    unittest.main()