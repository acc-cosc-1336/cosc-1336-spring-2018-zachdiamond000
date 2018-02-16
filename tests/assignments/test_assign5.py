import unittest

from src.assignments.assignment5 import recursive_decimal_binary

#write import for decimal to binary function


class Test_Assign4(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(1,1)
        
    def test_recursive_decimal_binary_w_base_case(self):
        self.assertEqual('00000000', recursive_decimal_binary(0,7))

    def test_recursive_decimal_binary_w_value_65(self):
        self.assertEqual('01000001', recursive_decimal_binary(65,7))

    def test_recursive_decimal_binary_w_value_86(self):
        self.assertEqual('01010110', recursive_decimal_binary(86,7))

    def test_recursive_decimal_binary_w_value_128(self):
        self.assertEqual('10000000', recursive_decimal_binary(128,7))

    def test_recursive_decimal_binary_w_value_255(self):
        self.assertEqual('11111111', recursive_decimal_binary(255,7))

    #write test cases with arguments 85 and 63 for recursive_decimal_binary function

unittest.main(verbosity=2)
