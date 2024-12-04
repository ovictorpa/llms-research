import unittest
from your_module import is_palindrome, make_palindrome  # Replace with the actual module name

class TestIsPalindrome(unittest.TestCase):
    def test_true_palindromes(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("madam"))

    def test_false_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("abcdefg"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


class TestMakePalindrome(unittest.TestCase):
    def test_single_character(self):
        input_string = "a"
        expected_output = "a" + "a"[::-1]
        self.assertEqual(make_palindrome(input_string), expected_output)

    def test_short_strings(self):
        input_string = "radar"
        expected_output = "radar" + "radar"[::-1]
        self.assertEqual(make_palindrome(input_string), expected_output)

    def test_long_strings(self):
        input_string = "hello world"
        expected_output = "hello world" + "olleh wodlh"[::-1]
        self.assertEqual(make_palindrome(input_string), expected_output)

    def test_empty_string(self):
        input_string = ""
        expected_output = ""
        self.assertEqual(make_palindrome(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()