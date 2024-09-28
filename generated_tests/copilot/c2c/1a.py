import unittest
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

class TestHasCloseElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 1.0))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 1.0))

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 3.0, 5.0], 1.0))

    def test_some_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0], 1.5))

    def test_all_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.1, 1.2], 0.5))

if __name__ == '__main__':
    unittest.main()