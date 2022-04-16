import argparse
import sys

class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score (int): score of player
    """
    # optional parameter of name
    def __init__(self, name = 'Player 1'):
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            name (str): user inputted name
        """
        pass
    
    def __iadd__(self, other):
        """Used to add the scores at the end of each round. Total score per game
        will be stored in a dictionary with a key being a game # and value being
        the total score. 
        
        Args:
            other (int): round score to be added to current score
        
        Return:
            dictionary of scores
        """
        pass
    
    def coordinates(self):
        """The players inputted coordinates which the arrow is aimed and fired 
        at. Coordinate is determined based on relative position of shot to 
        center and accounts wind interference.
        
        Return:
            coordinate affected by wind
        """
        pass
    
    def score(self):
        """Score taken from coordinate shot landed on. Score calls validate_shot
        to distribute points based on where shot landed. 
        """
        # scores in each round will be stored in a dictionary with the rounds 
        # being the keys and the scores as the values.
        # determine score using conditional expressions, if _ unit from the bullseye then assign _ points
        
    def turn(self):
        """Prompts player for desired coordinates and makes sure inputted 
        coordinates are valid.
        """
        pass         
        
class ComputerPlayer(HumanPlayer):
    """Represents a computer player 

    Attributes:
        cname (str): name for computer player
    """
    
    def __init__(self, cname):
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        super().__init__()
        
    def turn(self):
        """Overides human and generates random coordinates within bounds 
        to shoot.
        """         
        
def round():
    """Initiates one round of the game.
    """
    pass

def wind_strength():
    """Determines the strength and direction at which the wind is occuring.
    
    Return:
        wind strength which consists of strength and direction
    """
    # randomly generate wind direction of 1-2 units in NESW direction

def validate_shot():
    """Determines distance from bullseye.
    
    Return:
        affected coordinates distance from bullseye
    """
    pass

def game_over():
    """Game is over and determines the winner. 
    
    Return:
        boolean: false if game is not over true if game is over
    """
    # use f-strings to display the name and total score over all 3 rounds
    
def main():
    """Plays one round of the archery game and calls necessary 
    methods/functions.
    """
    pass 

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