import unittest
from c2c._38a import encode_cyclic, decode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abcdef"), "bcadef")
        self.assertEqual(encode_cyclic("abcde"), "bcade")
        self.assertEqual(encode_cyclic("abcd"), "bcad")
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(encode_cyclic("ab"), "ab")
        self.assertEqual(encode_cyclic("a"), "a")
        self.assertEqual(encode_cyclic(""), "")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("bcadef"), "abcdef")
        self.assertEqual(decode_cyclic("bcade"), "abcde")
        self.assertEqual(decode_cyclic("bcad"), "abcd")
        self.assertEqual(decode_cyclic("bca"), "abc")
        self.assertEqual(decode_cyclic("ab"), "ab")
        self.assertEqual(decode_cyclic("a"), "a")
        self.assertEqual(decode_cyclic(""), "")

if __name__ == '__main__':
    unittest.main()