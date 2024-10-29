import unittest
from humaneval_prompts.c2c.1a import has_close_elements

class TestHasCloseElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 1.0))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 1.0))

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 3.0, 5.0], 1.0))

    def test_some_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.5, 3.0], 0.6))

    def test_all_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.1, 1.2], 0.2))

if __name__ == '__main__':
    unittest.main()