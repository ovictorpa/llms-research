import unittest

class TestFilterByPrefix(unittest.TestCase):

    def test_filter_empty_list(self):
        strings = []
        prefix = 'a'
        expected_result = []
        self.assertEqual(filter_by_prefix(strings, prefix), expected_result)

    def test_filter_no_match(self):
        strings = ['apple', 'banana', 'cherry']
        prefix = 'd'
        expected_result = []
        self.assertEqual(filter_by_prefix(strings, prefix), expected_result)

    def test_filter_single_match(self):
        strings = ['abc', 'xyz', 'def']
        prefix = 'a'
        expected_result = ['abc']
        self.assertEqual(filter_by_prefix(strings, prefix), expected_result)

    def test_filter_multiple_matches(self):
        strings = ['apple', 'apricot', 'acorn', 'array']
        prefix = 'a'
        expected_result = ['apple', 'apricot', 'acorn', 'array']
        self.assertEqual(filter_by_prefix(strings, prefix), expected_result)

if __name__ == '__main__':
    unittest.main()