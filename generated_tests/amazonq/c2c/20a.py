import unittest
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    min_distance = float('inf')
    
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j:
                distance = abs(num1 - num2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = tuple(sorted([num1, num2]))
    
    return closest_pair

class TestFindClosestElements(unittest.TestCase):
    def test_find_closest_elements(self):
        # Test case 1: Empty list
        self.assertIsNone(find_closest_elements([]))

        # Test case 2: Single element list
        self.assertIsNone(find_closest_elements([1.0]))

        # Test case 3: Two elements with equal values
        self.assertEqual(find_closest_elements([1.0, 1.0]), (1.0, 1.0))

        # Test case 4: Two elements with different values
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))

        # Test case 5: Multiple elements with distinct values
        self.assertEqual(find_closest_elements([1.0, 2.5, 3.9, 4.1, 5.0]), (3.9, 4.1))

        # Test case 6: Multiple elements with duplicate values
        self.assertEqual(find_closest_elements([1.0, 2.0, 2.0, 3.0, 3.0, 3.0]), (2.0, 2.0))

        # Test case 7: Negative numbers
        self.assertEqual(find_closest_elements([-1.0, 1.0, 2.0, -2.0]), (-2.0, -1.0))

        # Test case 8: Large numbers
        self.assertEqual(find_closest_elements([1e10, 1e10 + 1, 1e10 + 2]), (1e10, 1e10 + 1))

if __name__ == '__main__':
    unittest.main()
