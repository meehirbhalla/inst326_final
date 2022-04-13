import argparse


class HumanPlayer:
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
    """
    def __init__(self, name):
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
        
        """
        pass
    
    def __add__(self):
        """Used to add the scores at the end of each round. Total score per game
        will be stored in a dictionary witha key being a game # and value being
        the total score. 
        
        Args:
        
        """
        pass

    def windStrength(self):
        """Determines the strength and direction at which the wind is occuring
        
        Args:
        
        """
        pass
    
    def coordinates(self, x, y):
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
        """Validates shot on the board and distributes points based on
        coordinates
        
        Args:
        
        """
        pass
    
    def score(self):
        """Score taken from coordinate shot landed on. Coordinate is determined 
        based on relative position of shot to center and accounts wind
        interference
        
        Args:
        """
        pass
    
    def playRound(self):
        """Initiates one round of the game.
        
        Args:
        
        """
        pass
        
    def winner(self):
        """Game is over and determines the winner
        
        Args:
        
        """
        pass
        
    
        
class ComputerPlayer(HumanPlayer):
    """Represents a computer player 

    Args:
        HumanPlayer (_type_): _description_
    """
    
    def __init__(self, name):
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        super().__init__()
        
    def randomize_Coordinates(self):
        """Overides Human
        """


