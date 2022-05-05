import argparse
import sys
import random

class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score (int): score of player
    """
    # utilizes optional parameters of name
    def __init__(self, name = 'Player 1', score):
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            name (str): user inputted name
        """
        
        self.name = name
        self.score = score
    
    def round(self):
        """Initiates one round of the game.
        """
        rounds = 0 
        player = 0

        #in the begining of each round anounce the current round, and display display score

        while game_over() == False:
            # keep initiating rounds of the game
            # there should be a total of three rounds, and the first player to win 2 rounds win, but as long as the game is not over keep initiating
            # announce whose turn it is
            # display wind strength

    # __iadd__ magic method to add to dictionary of scores per round
    def __iadd__(self, other):
        """Used to add the scores at the end of each round. Total score per game
        will be stored in a dictionary with a key being a game # and value being
        the total score. 
        
        Args:
            other (int): round score to be added to current score
        
        Return:
            dictionary of scores
        """
         # uses the __iadd__ magic method to calculate the score and add to
         # dictionary of scores each round
        pass
    
    def coordinates(self):
        """The players inputted coordinates which the arrow is aimed and fired 
        at. Coordinate is determined based on relative position of shot to 
        center and accounts wind interference.
        
        Return:
            coordinate affected by wind
        """
        player_input = input (f'{self.name}, Please enter a coordinate: ')
        
        return player_input

    def score(self):
        """Score taken from coordinate shot landed on. Score calls validate_shot
        to distribute points based on where shot landed. 
        """
        # scores in each round will be stored in a dictionary with the rounds 
        # being the keys and the scores as the values.
        # determine score using conditional expressions, 
        # if _ unit from the bullseye then assign _ points
        
    def turn(self):
        """Prompts player for desired coordinates and makes sure inputted 
        coordinates are valid.
        """
    
        # use sequence unpacking to access the x (letter) and y (number) to interpret desired coordinate
        # e.g., c3 would unpack to x = c and y = 3
        
        # prompt player 
        player_input = input (f'{self.name}, Please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-5: ')
        x,y = player_input
        
        print (f'Coordinate selected: ,{x},{y}')

  
class ComputerPlayer(HumanPlayer):
    # inherits all the methods from the human class
    """Represents a computer player 

    Attributes:
        cname (str): name for computer player
    """
    
    # optional parameter for computer name 
    def __init__(self, cname = 'Computer'):
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        # uses super to call the init method from the human class
        super().__init__()
        
    def turn(self):
        """Overides human and generates random coordinates within bounds 
        to shoot.
        """         
        # overrides the turn method in the human class since computer turn randomly generates a coordinate to shoot


def wind_strength():
    """Determines the strength and direction at which the wind is occuring.
    
    Return:
        wind strength which consists of strength and direction
    """
    # randomize direction
    direction = ['N', 'S', 'E', 'W']
    print(random.choice(direction))
    
    # randomize wind strength
    strength = [1, 2]
    
    
    
    # randomly generate wind direction of 1-2 units in NESW direction

def validate_shot():
    """Determines distance from bullseye.
    
    Return:
        affected coordinates distance from bullseye
    """
    
    # determine distance using the x and y coordinates of the affected coordinate
    # in relation to the bullseye (c3)

def game_over():
    """Game is over and determines the winner. 
    
    Return:
        boolean: false if game is not over true if game is over
    """
    # use f-strings to display the name and total score over all 3 rounds
    # use custom list sorting to list best performing rounds by score
    
def main():
    """Plays one round of the archery game and calls necessary 
    methods/functions.
    """
    pass 

# argument parser in order to use command line arguments 
# (player name and desired target) 
def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: name of player
        - str: desired position on target
    
    Args:
        arglist (list of str): arguments from command line
    
    Returns:
        namespace: parsed arguments
    """ 
    pass

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])