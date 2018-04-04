#Write an import statement for the Python random module
import random



class Die:

    
    sides = 6
    die = random.randint(1,sides)

    def __init__(self):
        '''
        Define a constructor method with one attribute sides with a values of 6.
        '''
        self.sides = 6
        

    def roll(self):
        '''
        Define a roll method that virtually rolls a die and returns the value.
        '''
        
        self.die = random.randint(1,self.sides)

        
    def get_roll(self):
        return self.die
