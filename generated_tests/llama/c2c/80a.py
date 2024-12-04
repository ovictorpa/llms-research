import unittest

class TestHappy(unittest.TestCase):
    def test_short_strings(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("ab"))

    def test_no_repeats(self):
        self.assertTrue(is_happy("abc"))
        self.assertTrue(is_happy("abcd"))

    def test_single_repeats(self):
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("aabbc"))

    def test_consecutive_repeats(self):
        self.assertFalse(is_happy("aabbcc"))
        self.assertFalse(is_happy("xyzzyyzz"))

    def test_mixed_repeats(self):
        self.assertFalse(is_happy("abcaaa"))
        self.assertFalse(is_happy("xyyzabc"))

if __name__ == '__main__':
    unittest.main()