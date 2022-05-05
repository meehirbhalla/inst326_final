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
    
    def coordinates(self, selected_coordinate):
        """The players inputted coordinates which the arrow is aimed and fired 
        at. Coordinate is determined based on relative position of shot to 
        center and accounts wind interference.
        
        Return:
            coordinate affected by wind
        """
        
        wind = wind_strength(selected_coordinate)
        
        x, y = self.selected_coordinate
        
        if wind == 'N':
            self.final_coordinate = self.selected_coordinate + 1
        if wind == 'S':
            self.final_coordinate = self.selected_coordinate - 1
        if wind == 'E':
            self.final_coordinate = self.selected_coordinate + 10
        if wind == 'W':
            self.final_coordinate = self.selected_coordinate - 10
            
    
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
        while(player_input not in valid_input):
            player_input = input (f'{self.name}, Please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-5: ')
            
        x,y = player_input
        
        # unpack x and y from player input
        if x in player_input == 'A':
            self.elected_coordinate = 1 + y
        if x in player_input == 'B':
            self.selected_coordinate = 2 + y
        if x in player_input == 'C':
            self.selected_coordinate = 3 + y
        if x in player_input == 'D':
            self.selected_coordinate = 4 + y
        if x in player_input == 'E':
            self.selected_coordinate = 5 + y
        
        print (f'Coordinate selected: ,{player_input}')
        
    
    def wind_strength(self, selected_coordinate):
        """Determines the direction at which the wind is occuring.
        
        Return:
            wind strength which consists of direction
        """
        # randomize direction
        direction = ['N', 'S', 'E', 'W']
    
        # for A as x coordinate
        if (self.selected_coordinate == 11):
            self.random_direction = (random.choice(direction[0::2]))
        elif (self.selected_coordinate == 12) or (self.selected_coordinate == 13) or (self.selected_coordinate == 14):
            self.random_direction = (random.choice(direction[0::2]))
        else:
            self.random_direction = (random.choice(direction[1::2]))
            
        # for B, C, and D as x coordinate
        if (self.selected_coordinate == 21) or (self.selected_coordinate == 31) or (self.selected_coordinate == 41):
            dont_include = 1
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        elif (self.selected_coordinate == 25) or (self.selected_coordinate == 35) or (self.selected_coordinate == 45):
            dont_include = 0
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        else:
            self.random_direction = (random.choice(direction))
            
        # for E as x coordinate
        if (self.selected_coordinate == 51):
            self.random_direction = (random.choice(direction[0::3]))
        elif (self.selected_coordinate == 52) or (self.selected_coordinate == 53) or (self.selected_coordinate == 54):
            dont_include = 2
            self.random_direction = (random.choice(direction[:dont_include] + direction[dont_include+1:]))
        else:
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