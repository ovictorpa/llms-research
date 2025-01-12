import unittest

def how_many_times(string: str, substring: str) -> int:
    times = 0
    substring_length = len(substring)
    
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:
            times += 1
    
    return times

class TestHowManyTimes(unittest.TestCase):
    def test_how_many_times(self):
        # Test case 1: Substring not in string
        self.assertEqual(how_many_times("hello world", "xyz"), 0)

        # Test case 2: Substring appears once
        self.assertEqual(how_many_times("hello world", "world"), 1)

        # Test case 3: Substring appears multiple times

        # Test case 4: Overlapping substrings
        self.assertEqual(how_many_times("aaaaa", "aa"), 4)

        # Test case 5: Empty substring
        self.assertEqual(how_many_times("hello world", ""), len("hello world") + 1)

        # Test case 6: Empty string
        self.assertEqual(how_many_times("", "abc"), 0)

        # Test case 7: Both string and substring are empty
        self.assertEqual(how_many_times("", ""), 1)

        # Test case 8: Substring is longer than string
        self.assertEqual(how_many_times("short", "longer string"), 0)

        # Test case 9: Case sensitivity

        # Test case 10: Special characters
        self.assertEqual(how_many_times("!@#$%^&*()!@#$%^&*()", "!@#$%^&*()"), 2)

if __name__ == '__main__':
    unittest.main()
