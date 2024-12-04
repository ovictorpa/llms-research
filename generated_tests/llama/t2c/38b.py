import unittest
from your_module import encode_cyclic, decode_cyclic  # Replace 'your_module' with the actual name of the module

class TestEncodeDecodeCyclic(unittest.TestCase):

    def test_encode_decode_cyclic_1(self):
        input_string = 'abcdefg'
        encoded_string = encode_cyclic(input_string)
        self.assertEqual(decode_cyclic(encoded_string), input_string)

    def test_encode_decode_cyclic_2(self):
        input_string = 'abcde'
        encoded_string = encode_cyclic(input_string)
        self.assertEqual(decode_cyclic(encoded_string), input_string)

if __name__ == '__main__':
    unittest.main()