#write import statement for Die class
from die import Die


class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        
        self.die1.roll()
        self.die2.roll()

        print('Die1: ', str(self.die1.get_roll()),'Die2: ', str(self.die2.get_roll()))
        
        while self.die1.get_roll()!= self.die2.get_roll():
            self.die1.roll()
            self.die2.roll()
            print('Die1: ', str(self.die1.get_roll()),'Die2: ', str(self.die2.get_roll()))
            

            
