import argparse
import sys

class Player:
    """
    
    """    
class HumanPlayer:
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
    """
    #Include score as a attribute for player
    #Think about the methods that belong in HumanPlayer and those that belong 
    #outside it. Validate_Shot for example. 
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
        """
        pass
    
    def coordinates(self):
        """The players chosen coordinates that the arrow is aimed and fired at
        
        Args:
        
        """
        pass
    
    def rounds(self):
        """The rounds which are played in the game 
        
        Args:
        
        """

        pass 
    
    def validate_shot(self):
        """Validates shot on the board
        
        Args:
        
        """
        pass
    
    def score(self):
        """Score taken from coordinate shot landed on. Coordinate is determined 
        based on relative position of shot to center and accounts wind
        interference. Score calls validate_shot to distribute points based on
        where shot landed. 
        
        Args:
        """
        pass
          
    def turn(self):
        """Take turns between human and computer players.
        """         
    #Add a class or method to take turns between player and computer
        
class ComputerPlayer(HumanPlayer):
    """Represents a computer player 

    Args:
        HumanPlayer (HumanPlayer): _description_
    """
    
    def __init__(self, name):
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        super().__init__()
        
    def randomize_Coordinates(self, x, y ):
        """Overides Human
        """
    
    def turn(self):
        """Take turns between human and computer players.
        """         


def winner():
    """Game is over and determines the winner.   
    """
    
def play_round():
    """Initiates one round of the game. Calls round method to initiate a 
    players turn.  
    """
    pass

def wind_strength():
    """Determines the strength and direction at which the wind is occuring
    """
    #Think about where your storing wind strength 
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