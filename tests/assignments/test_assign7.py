import unittest
#write the import for function for assignment7 sum_list_values
from assignment7 import sum_list_values

class Test_Assign7(unittest.TestCase):

    def sample_test(self):
        self.assertEqual(1,1)

    #create a test for the sum_list_values function with list elements:
    # bill 23 16 19 22
    def test_sum_list_values_w_list(self):
        self.assertEqual((80), sum_list_values(['Bill',23,16,19,22]))
    
unittest.main(verbosity=3)
