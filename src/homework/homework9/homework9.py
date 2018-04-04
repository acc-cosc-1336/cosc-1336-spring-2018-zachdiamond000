from player import Player
from die import Die
#write import statements for Player and Die class

#Create an instance of the Main class and call/execute the roll_doubles method


again = 'y'
Player1 = Player()

while again == 'y':
    Player1.roll_doubles()
        

    again = input("Would you like to roll again? Y/N....")


