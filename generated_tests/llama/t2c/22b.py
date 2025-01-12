from typing import List, Any

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_single_value(self):
        result = filter_integers([5])
        self.assertEqual(result, [5])

    def test_filter_integers_multiple_values(self):
        result = filter_integers([1, 2, 3, 'abc', {}, []])
        expected_result = [1, 2, 3]
        self.assertEqual(result, expected_result)

    def test_filter_integers_all_non_integers(self):
        result = filter_integers(['a', 3.14, 'b'])
        self.assertEqual(result, [])

    def test_filter_integers_empty_list(self):
        with self.assertRaises(ValueError):  # Assuming the function will raise an error if the input list is empty
            filter_integers([])

    def test_filter_integers_non_list_input(self):
        with self.assertRaises(TypeError):  # Assuming the function will raise an error if the input is not a list
            filter_integers('not a list')

if __name__ == '__main__':
    unittest.main()