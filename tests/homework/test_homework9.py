import unittest
from die import Die

class TestHomework9(unittest.TestCase):

    def test_rolls_values_1_to_6(self):
        '''
        Write a test case to ensure that the Die class only rolls values from 1 to 6

        '''
        die = Die()
        sides = 6
        
        self.assertTrue(1 <= die.get_roll()<= 6)
        

