import unittest
from c2c.81a import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_all_grades(self):
        grades = [4.0, 3.8, 3.5, 3.2, 2.9, 2.5, 2.2, 1.9, 1.5, 1.2, 0.9, 0.5, 0.0]
        expected = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([4.0]), ["A+"])
        self.assertEqual(numerical_letter_grade([3.8]), ["A"])
        self.assertEqual(numerical_letter_grade([3.5]), ["A-"])
        self.assertEqual(numerical_letter_grade([3.2]), ["B+"])
        self.assertEqual(numerical_letter_grade([2.9]), ["B"])
        self.assertEqual(numerical_letter_grade([2.5]), ["B-"])
        self.assertEqual(numerical_letter_grade([2.2]), ["C+"])
        self.assertEqual(numerical_letter_grade([1.9]), ["C"])
        self.assertEqual(numerical_letter_grade([1.5]), ["C-"])
        self.assertEqual(numerical_letter_grade([1.2]), ["D+"])
        self.assertEqual(numerical_letter_grade([0.9]), ["D"])
        self.assertEqual(numerical_letter_grade([0.5]), ["D-"])
        self.assertEqual(numerical_letter_grade([0.0]), ["E"])

    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_boundary_values(self):
        self.assertEqual(numerical_letter_grade([3.7]), ["A-"])
        self.assertEqual(numerical_letter_grade([3.3]), ["B+"])
        self.assertEqual(numerical_letter_grade([3.0]), ["B"])
        self.assertEqual(numerical_letter_grade([2.7]), ["B-"])
        self.assertEqual(numerical_letter_grade([2.3]), ["C+"])
        self.assertEqual(numerical_letter_grade([2.0]), ["C"])
        self.assertEqual(numerical_letter_grade([1.7]), ["C-"])
        self.assertEqual(numerical_letter_grade([1.3]), ["D+"])
        self.assertEqual(numerical_letter_grade([1.0]), ["D"])
        self.assertEqual(numerical_letter_grade([0.7]), ["D-"])
        self.assertEqual(numerical_letter_grade([0.1]), ["D-"])

if __name__ == '__main__':
    unittest.main()