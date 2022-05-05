import argparse
import sys
import random

# valid positions on the target
POTENTIAL_SPOTS = {
    'A1': 1, 
    'A2': 2,
    'A3': 3,
    'A4': 4,
    'A5': 5,
    'B1': 6,
    'B2': 7,
    'B3': 8,
    'B4': 9,
    'B5': 10,
    'C1': 11,
    'C2': 12,
    'C3': 13,
    'C4': 14,
    'C5': 15,
    'D1': 16,
    'D2': 17,
    'D3': 18,
    'D4': 19,
    'D5': 20,
    'E1': 21,
    'E2': 22,
    'E3': 23,
    'E4': 24,
    'E5': 25
}

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
    
    def coordinates(self, x_coordinate, y_coordinate):
        """The players inputted coordinates which the arrow is aimed and fired 
        at. Coordinate is determined based on relative position of shot to 
        center and accounts wind interference.
        
        Return:
            coordinate affected by wind
        """
        
        wind_strength(self.player_input)
        
        wind = self.random_direction
        
        if wind == 'N':
            self.y_coordinate = self.y_coordinate + 1
        if wind == 'S':
            self.y_coordinate = self.y_coordinate - 1
        if wind == 'E':
            self.x_coordinate = self.x_coordinate + 1
        if wind == 'W':
            self.x_coordinate = self.x_coordinate + 1
    
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
        valid_input = ['A1', 'A2', 'A3', 'A4', 'A5',
                       'B1', 'B2', 'B3', 'B4', 'B5',
                       'C1', 'C2', 'C3', 'C4', 'C5',
                       'D1', 'D2', 'D3', 'D4', 'D5',
                       'E1', 'E2', 'E3', 'E4', 'E5']
        
        # ensure valid input
        while(self.player_input not in valid_input):
            self.player_input = input (f'{self.name}, Please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-5: ')
            
        x,y = self.player_input
        
        # unpack x and y from player input
        self.x_coordinate = x
        self.y_coordinate = y
        
        print (f'Coordinate selected: ,{self.x_coordinate},{self.y_coordinate}')
        
    
    def wind_strength(self, x_coordinate, y_coordinate):
        """Determines the direction at which the wind is occuring.
        
        Return:
            wind strength which consists of direction
        """
        # randomize direction
        direction = ['N', 'S', 'E', 'W']
    
        # for A as x coordinate
        if (self.x_coordinate == 'A') and (self.y_coordinate == 1):
            self.random_direction = (random.choice(direction[0::2]))
        if (self.x_coordinate == 'A') and (self.y_coordinate == 2) or (self.y_coordinate == 3) or (self.y_coordinate == 4):
            self.random_direction = (random.choice(direction[0:2]))
        if (self.x_coordinate == 'A') and (self.y_coordinate == 5):
            self.random_direction = (random.choice(direction[1::2]))
            
        # for B, C, and D as x coordinate
        if (self.x_coordinate == 'B') or (self.x_coordinate == 'C') or (self.x_coordinate == 'D') and (self.y_coordinate == 2) or (self.y_coordinate == 3) or (self.y_coordinate 4):
            self.random_direction = (random.choice(direction))
        if (self.x_coordinate == 'B') or (self.x_coordinate == 'C') or (self.x_coordinate == 'D') and (self.y_coordinate == 1):
            dont_include = 1
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        if (self.x_coordinate == 'B') or (self.x_coordinate == 'C') or (self.x_coordinate == 'D') and (self.y_coordinate == 5):
            dont_include = 0
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        
        # for E as x coordinate
        if (self.x_coordinate == 'E') and (self.y_coordinate == 1):
            self.random_direction = (random.choice(direction[0::3]))
        if (self.x_coordinate == 'E') and (self.y_coordinate == 2) or (self.y_coordinate == 3) or (self.y_coordinate == 4):
            dont_include = 2
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        if (self.x_coordinate == 'E') and (self.y_coordinate == 5):
            self.random_direction = (random.choice(direction[1::3]))
        

  
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


def validate_shot():
    """Determines distance from bullseye.
    
    Return:
        affected coordinates distance from bullseye
    """
    bullseye = 'C3'
    
    if 
    # determine distance using the x and y coordinates of the affected coordinate

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