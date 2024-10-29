import unittest

def move_one_ball(arr):
    """
    Determine if it is possible to sort the array in non-decreasing order by performing right shift operations.
    A right shift operation means shifting all elements of the array by one position to the right.
    The last element of the array moves to the start position.

    Examples:
    >>> move_one_ball([3, 4, 5, 1, 2])
    True
    >>> move_one_ball([3, 5, 4, 1, 2])
    False
    >>> move_one_ball([1, 2, 3, 4, 5])
    True
    >>> move_one_ball([5, 1, 2, 3, 4])
    True
    >>> move_one_ball([4, 5, 1, 2, 3])
    True
    >>> move_one_ball([1, 3, 2])
    False
    """
    n = len(arr)
    for i in range(n):
        if arr[i:] + arr[:i] == sorted(arr):
            return True
    return False

class TestMoveOneBall(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
    
    def test_example_2(self):
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)
    
    def test_example_3(self):
        self.assertEqual(move_one_ball([1, 2, 3, 4, 5]), True)
    
    def test_example_4(self):
        self.assertEqual(move_one_ball([5, 1, 2, 3, 4]), True)
    
    def test_example_5(self):
        self.assertEqual(move_one_ball([4, 5, 1, 2, 3]), True)
    
    def test_example_6(self):
        self.assertEqual(move_one_ball([1, 3, 2]), False)
    
    def test_empty_list(self):
        self.assertEqual(move_one_ball([]), True)
    
    def test_single_element(self):
        self.assertEqual(move_one_ball([1]), True)
    
    def test_two_elements_sorted(self):
        self.assertEqual(move_one_ball([1, 2]), True)
    
    def test_two_elements_unsorted(self):
        self.assertEqual(move_one_ball([2, 1]), True)
    
    def test_large_sorted(self):
        self.assertEqual(move_one_ball(list(range(1000))), True)
    
    def test_large_unsorted(self):
        self.assertEqual(move_one_ball(list(range(500, 1000)) + list(range(500))), True)

if __name__ == '__main__':
    unittest.main()