import unittest

def numerical_letter_grade(grades):
    """
    Convert a list of GPAs to their corresponding letter grades based on the following scale:
    
    GPA | Letter grade
    4.0 | A+
    > 3.7 | A
    > 3.3 | A-
    > 3.0 | B+
    > 2.7 | B
    > 2.3 | B-
    > 2.0 | C+
    > 1.7 | C
    > 1.3 | C-
    > 1.0 | D+
    > 0.7 | D
    > 0.0 | D-
    0.0 | E
    
    Examples:
    >>> numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
    ['A+', 'B', 'C-', 'C', 'A-']
    """
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])
    
    def test_all_grades(self):
        self.assertEqual(numerical_letter_grade([4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.1, 0.0]),
                         ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'])
    
    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])
    
    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([3.5]), ['A-'])
    
    def test_edge_cases(self):
        self.assertEqual(numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]),
                         ['A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'])

if __name__ == '__main__':
    unittest.main()