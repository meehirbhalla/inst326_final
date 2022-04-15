import argparse
import sys

class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score (int): score of player
    """
    def __init__(self, name):
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
        """The players inputted coordinates which the arrow is aimed and fired at.
        
        Return:
            selected coordinates. 
        """
        pass
    
    def score(self):
        """Score taken from coordinate shot landed on. Coordinate is determined 
        based on relative position of shot to center and accounts wind
        interference. Score calls validate_shot to distribute points based on
        where shot landed. 
        """
        pass
          
    def turn(self):
        """Prompts player for desired coordinates.
        """         
        
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
        
    def randomize_Coordinates(self, x, y ):
        """Overides Human and generates random coordinates to shoot.
        """         
        
def round():
    """Initiates one round of the game.
    """
    pass

def wind_strength():
    """Determines the strength and direction at which the wind is occuring
    """
    pass

def validate_shot():
    """Validates a shot on the board.
    """
    pass

def winner():
    """Game is over and determines the winner.   
    """
    
def main():
    """Plays one round of the archery game and calls necessary methods/functions.
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