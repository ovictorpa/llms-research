import unittest

def match_parens(lst):
    ''' 
    You are given a list of two strings, both strings consist of open parentheses '(' or close parentheses ')' only. 
    Your job is to check if it is possible to concatenate the two strings in some order, that the resulting string will be good. 
    A string S is considered to be good if and only if all parentheses in S are balanced. 
    For example: the string '(())()' is good, while the string '())' is not. 
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise. 
    
    Examples: 
    match_parens(['()(', ')']) == 'Yes' 
    match_parens([')', ')']) == 'No' 
    '''
    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    s1, s2 = lst
    return 'Yes' if is_balanced(s1 + s2) or is_balanced(s2 + s1) else 'No'

class TestMatchParens(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
    
    def test_example_2(self):
        self.assertEqual(match_parens([')', ')']), 'No')
    
    def test_balanced(self):
        self.assertEqual(match_parens(['(())', '()']), 'Yes')
    
    def test_unbalanced(self):
        self.assertEqual(match_parens(['(()', '())']), 'No')
    
    def test_empty_strings(self):
        self.assertEqual(match_parens(['', '']), 'Yes')
    
    def test_single_open_close(self):
        self.assertEqual(match_parens(['(', ')']), 'Yes')
    
    def test_single_close_open(self):
        self.assertEqual(match_parens([')', '(']), 'No')
    
    def test_nested(self):
        self.assertEqual(match_parens(['(((', ')))']), 'Yes')
    
    def test_all_open(self):
        self.assertEqual(match_parens(['(((', '(((']), 'No')
    
    def test_all_close(self):
        self.assertEqual(match_parens([')))', ')))']), 'No')

if __name__ == '__main__':
    unittest.main()