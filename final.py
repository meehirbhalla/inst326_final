import argparse
import sys

class Player:
    """Class for archery player.
    
    Attributes:
        name (str): player name
    """   
def __init__(self, name):
    """Function that will initialize the objects that were represented in
        the attributes.
        
    Args:
        name (str): user inputted name
    """
    self.name = name

def turn(self):
        """Take turns between human and computer players.
        """
        
class HumanPlayer(Player):
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score (int): score of player
    """
    #Include score as a attribute for player
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
        
class ComputerPlayer(Player):
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

def validate_shot():
    """Validates a shot on the board.
    """
    pass

def play_rounds():
    """The rounds which are played in the game.
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