import unittest

class TestIsHappy(unittest.TestCase):

    def test_is_happy_1(self):
        self.assertFalse(is_happy("a"))

    def test_is_happy_2(self):
        self.assertFalse(is_happy("aa"))

    def test_is_happy_3(self):
        self.assertTrue(is_happy("abcd"))

    def test_is_happy_4(self):
        self.assertFalse(is_happy("aabb"))

    def test_is_happy_5(self):
        self.assertTrue(is_happy("adb"))

    def test_is_happy_6(self):
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()