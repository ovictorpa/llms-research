import unittest

class TestMoveOneBall(unittest.TestCase):

    def test_move_one_ball_1(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_move_one_ball_2(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_move_one_ball_3(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_move_one_ball_4(self):
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))

    def test_move_one_ball_5(self):
        self.assertTrue(move_one_ball([4, 5, 1, 2, 3]))

    def test_move_one_ball_6(self):
        self.assertFalse(move_one_ball([1, 3, 2]))

if __name__ == '__main__':
    unittest.main()