import argparse
import sys
Rounds = 0
class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        name(str): Name of current player 
        score (int): score of player
    """
    # utilizes optional parameters of name
    def __init__(self, name = 'Player 1'): #KHALIIL
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            name (str): user inputted name
        """
        pass
    
    def round(self):
        """Initiates one round of the game.
        """
        pass

    # __iadd__ magic method to add to dictionary of scores per round
    def __iadd__(self, other):#BRICE
        """Used to add the scores at the end of each round. Total score per game
        will be stored in a dictionary with a key being a game # and value being
        the total score. 
        
        Args:
            other (int): round score to be added to current score
        
        Return:
            dictionary of scores
        """
        score_per_game = dict()
        
         # uses the __iadd__ magic method to calculate the score and add to
         # dictionary of scores each round
        pass
    
    def coordinates(self): #MEHIR
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
        # determine score using conditional expressions, 
        # if _ unit from the bullseye then assign _ points
        
    def turn(self):
        """Prompts player for desired coordinates and makes sure inputted 
        coordinates are valid.
        """
        # use sequence unpacking to access the x (letter) and y (number) to interpret desired coordinate
        # e.g., c3 would unpack to x = c and y = 3
  
        
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
<<<<<<< HEAD

=======
        
def round():#KHALIIL
    """Initiates one round of the game.
    """
    Rounds = Rounds + 1
    pass
>>>>>>> bcf7223 (Testing commit)

def wind_strength():#MEHIR
    """Determines the strength and direction at which the wind is occuring.
    
    Return:
        wind strength which consists of strength and direction
    """
    # randomly generate wind direction of 1-2 units in NESW direction

def validate_shot(): #MEHIR
    """Determines distance from bullseye.
    
    Return:
        affected coordinates distance from bullseye
    """
    # determine distance using the x and y coordinates of the affected coordinate
    # in relation to the bullseye (c3)

    #Calls the wind_strength() method to calculate location of shot from the 
    #center
    pass

def game_over():#BRICE
    """Game is over and determines the winner. 
    
    Return:
        boolean: false if game is not over true if game is over
    """
    player = HumanPlayer()
    #May need a function to determine winner 
    #How do I call score_per_game dict from here
    #best_score = max(player.score_per_game, key=player.score_per_game.get)
    #best_score = player.score_per_game.sort(key=lambda x: )
    if Rounds == 3:
        
        print(f"The winner is: {player.name} with a total score of: {player.__iadd__()}")
        print()
        return True
    else:
        return False
    # use f-strings to display the name and total score over all 3 rounds
    # use custom list sorting to list best performing rounds by score

def winner(player):
    
    pass

    
def main():#BRICE
    """Plays one round of the archery game and calls necessary 
    methods/functions.
    """
    #Isnt this doing the same thing as round()?
    # Will make a call to coordinates(), turn(), validate_shot(), score(), and 
    # game_over()
    pass 

# argument parser in order to use command line arguments 
# (player name and desired target) 
def parse_args(arglist):#Brice
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: name of player
        - str: desired position on target
    
    Args:
        arglist (list of str): arguments from command line
    
    Returns:
        namespace: parsed arguments
    """ 
    parser = argparse.ArgumentParser()
    parser.add_argument("Player1", help= "Name ofthe first player")
    parser.add_argument("Computer", help= "Name ofthe computer player")
    return parser.parse_args(arglist)
 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])