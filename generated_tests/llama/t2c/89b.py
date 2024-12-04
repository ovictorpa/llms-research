import unittest

class TestEncrypt(unittest.TestCase):

    def test_encrypt_1(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_encrypt_2(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_encrypt_3(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_encrypt_4(self):
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()