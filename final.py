import argparse

class HumanPlayer:
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score(integer): tracks the players total score 
    """
    #Include score as a attribute for player
    #Think about the methods that belong in HumanPlayer and those that belong 
    #outside it. Validate_Shot for example. 
    def __init__(self, name):
        self.name = name
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
        
        """
        pass
    
    def __iadd__(self): #Add additional argument for iadd, fix description
        """Used to add the scores at the end of each round. Total score per game
        will be stored in a dictionary with a key being a game # and value being
        the total score. 
        
        Args:
        
        """
        pass

    def wind_strength(self):
        """Determines the strength and direction at which the wind is occuring
        
        Args:
        
        """
        #Think about where your storing wind strength 
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
    
    def score(self):
        """Score taken from coordinate shot landed on. Coordinate is determined 
        based on relative position of shot to center and accounts wind
        interference. Score calls validate_shot to distribute points based on
        where shot landed. 
        
        Args:
        """
        pass
    
    def take_turn():
        """Initiates a turn for a player(human or computer)
    
        """
           
    #Add a class or method to take turns between player and computer
    #
#------------------------------------------------------------------------------#        

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
        
    def randomize_Coordinates(self, x, y ):
        """Overides Human
        """
        
#------------------------------------------------------------------------------#
    
    
def validate_shot(self):
    """Validates shot on the board
        
    Args:
    
    """
    pass

    
def play_round(self):
    """Initiates one round of the game. Calls round method to initiate a 
    players turn. 
        
    Args:
        
    """
    pass

def winner():
    """Game is over and determines the winner. 
        
    Args:
        
    """
    
