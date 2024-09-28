import unittest
from c2c.80a import is_happy  # Adjust the import statement as needed

class TestIsHappy(unittest.TestCase):

    def test_happy_string(self):
        self.assertTrue(is_happy("abcde"))

    def test_unhappy_string_adjacent(self):
        self.assertFalse(is_happy("aabcd"))

    def test_unhappy_string_one_apart(self):
        self.assertFalse(is_happy("abcdd"))

    def test_unhappy_string_two_apart(self):
        self.assertFalse(is_happy("abcda"))

    def test_short_string_happy(self):
        self.assertTrue(is_happy("abc"))

    def test_short_string_unhappy(self):
        self.assertFalse(is_happy("aba"))

    def test_two_character_string(self):
        self.assertFalse(is_happy("ab"))

    def test_single_character_string(self):
        self.assertFalse(is_happy("a"))

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_long_happy_string(self):
        self.assertTrue(is_happy("abcdefghijklmnopqrstuvwxyz"))

    def test_long_unhappy_string(self):
        self.assertFalse(is_happy("abcdefghijklmnopqrstuvwxyza"))

    def test_repeated_characters_happy(self):
        self.assertTrue(is_happy("abcabcabc"))

    def test_repeated_characters_unhappy(self):
        self.assertFalse(is_happy("abcabcabca"))

    def test_case_sensitivity(self):
        self.assertTrue(is_happy("aBcDe"))
        self.assertFalse(is_happy("AbCdA"))

if __name__ == '__main__':
    unittest.main()
