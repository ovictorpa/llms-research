import unittest

def is_happy(s):
    """
    Check if the string `s` is happy. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Examples:
    >>> is_happy("a")
    False
    >>> is_happy("aa")
    False
    >>> is_happy("abcd")
    True
    >>> is_happy("aabb")
    False
    >>> is_happy("adb")
    True
    >>> is_happy("xyy")
    False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True

class TestIsHappy(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(is_happy("a"), False)
    
    def test_example_2(self):
        self.assertEqual(is_happy("aa"), False)
    
    def test_example_3(self):
        self.assertEqual(is_happy("abcd"), True)
    
    def test_example_4(self):
        self.assertEqual(is_happy("aabb"), False)
    
    def test_example_5(self):
        self.assertEqual(is_happy("adb"), True)
    
    def test_example_6(self):
        self.assertEqual(is_happy("xyy"), False)
    
    def test_empty_string(self):
        self.assertEqual(is_happy(""), False)
    
    def test_length_two(self):
        self.assertEqual(is_happy("ab"), False)
    
    def test_all_distinct(self):
        self.assertEqual(is_happy("abcdef"), True)
    
    def test_all_same(self):
        self.assertEqual(is_happy("aaa"), False)
    
    def test_mixed(self):
        self.assertEqual(is_happy("abac"), True)

if __name__ == '__main__':
    unittest.main()