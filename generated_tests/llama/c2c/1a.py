import unittest
from your_module import has_close_elements  # Replace with the actual module name

class TestHasCloseElements(unittest.TestCase):
    def test_no_close_elements(self):
        numbers = [1.0, 2.5, 3.8]
        threshold = 0.1
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_close_elements_found(self):
        numbers = [1.0, 1.05, 1.1]
        threshold = 0.1
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_threshold_exceeded(self):
        numbers = [1.0, 2.5, 3.8]
        threshold = 10.0
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_empty_list(self):
        numbers = []
        threshold = 0.1
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_single_element_list(self):
        numbers = [1.0]
        threshold = 0.1
        self.assertFalse(has_close_elements(numbers, threshold))

if __name__ == '__main__':
    unittest.main()