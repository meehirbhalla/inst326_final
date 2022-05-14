import argparse
import sys
import random
from typing_extensions import Self

score_per_round = dict()

class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        score (int): score of player
        name(str): Name of current player 
    """
    # utilizes optional parameters of name
    def __init__(self, score, name = 'Player 1'): #KHALIIL
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            score(integer): score of player
            name (str): user inputted name
        """
        self.score = score
        self.name = name
    
    def round(self, rounds):
        """Initiates one round of the game.
        """
        rounds = 0 
        while game_over() == False:
            # in the begining of each round anounce the current round, and display current score 
            print(f"The current score is {score()}") 
            print(f"Round {rounds} of 3")
            # there should be a total of three rounds, and the first player to win 2 rounds wins, but as long as the game is not over keep initiating
            rounds += 1
            # announce whose turn it is
            print(f"{self.name}, it is your turn")
            # display wind strength
            print(f"The current wind direction is {wind_strength} ")
        
    # __iadd__ magic method to add to dictionary of scores per round
    def __iadd__(self, other):#BRICE
        """Used to add the scores at the end of each round. Total score in each
        round will be stored in a dictionary with a key being a round # and 
        value being the score. 
        
        Args:
            other (int): round score to be added to current score
        
        Return:
            Dictionary with total score accumulated per round
        """
        #score_per_game = dict()
        
        #self.score += other.score
        #score_per_round[Round] = self.score
        #Round += 1
        
        #return score_per_round
        
        #totalScore = 0
        #totalScore += self.score
        
        score_per_round = {}
        
        if round == 1:
            self.score = self.scores[round]
            score_per_round[0] = self.score
        elif round == 2:
            #check if round starts at 0 or 1
            self.score = self.scores[1] + other.scores[round]
            score_per_round[1] = self.score
        elif round == 3:
            self.score += self.score + other.scores[round]
            score_per_round[2] = self.score
        
        return score_per_round
        
        
         # uses the __iadd__ magic method to calculate the score and add to
         # dictionary of scores each round
        
    # Meehir
    def coordinates(self):
        """The players inputted coordinates which the arrow is aimed and fired 
        at. Coordinate is determined based on relative position of shot to 
        center and accounts wind interference.
        
        Return:
            coordinate affected by wind
        """ 
        # the final coordinate depends on the random wind direction's affect on the player_input
        if self.wind == 'N':
            self.final_coordinate = self.player_input + 1
        elif self.wind == 'S':
            self.final_coordinate = self.player_input - 1
        elif self.wind == 'E':
            self.final_coordinate = self.player_input + 10
        elif self.wind == 'W':
            self.final_coordinate = self.player_input - 10
            
    def score(self):
        """Score taken from coordinate shot landed on. Score calls validate_shot
        to distribute points based on where shot landed. 
        """
        # scores in each round will be stored in a dictionary with the rounds 
        # being the keys and the scores as the values.
        # determine score using conditional expressions, 
        # if _ unit from the bullseye then assign _ points
        scores = {}
        
        five_points = ['B2','B3','B4','C2','C4','E2','E3','E4']
        
        # accounts for bullseye, five, and one point shots
        if self.final_coordinate == 'C3':
            scores.append(10)
        elif self.final_coordinate in five_points:
            scores.append(5)
        else:
            scores.append(1)
        
        if validate_shot(player_input) == 0:
            points = 10
        elif validate_shot(player_input) == 1:
            points = 5
        elif validate_shot(player_input) == 2:
            points = 3
        else
            points = 0
        
        scores[round] = points
        
    # Meehir           
    def turn(self):
        """Prompts player for desired coordinates and makes sure inputted 
        coordinates are valid.
        
        Returns:
            self.player_input: player input represented as a number
        """
        # use sequence unpacking to access the x (letter) and y (number) to interpret desired coordinate
        # e.g., c3 would unpack to x = c and y = 3 and ultimately x = 3 and y = 3
        
        # possible inputs given wind direction
        N = ['a1', 'a2', 'a3', 'a4' 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4']
        S = ['a2', 'a3', 'a4', 'a5', 'b2', 'b3', 'b4', 'b5', 'c2', 'c3', 'c4', 'c5', 'd2', 'd3', 'd4', 'd5', 'e2', 'e3', 'e4', 'e5']
        E = ['a1', 'a2', 'a3', 'a4', 'a5' , 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5']
        W = ['b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']
        
        # prompts users for coordinate with restrictions applied
        if self.wind == 'North':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
            while self.player_input.lower() not in N:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
        elif self.wind == 'South':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
            while self.player_input.lower() not in S:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
        elif self.wind == 'East':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
            while self.player_input.lower() not in E:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
        elif self.wind == 'West':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')
            while self.player_input.lower() not in W:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')

        # convert to lowercase
        self.player_input = self.player_input.lower()
        
        # unpack inputted coordinates
        x,y = self.player_input  
        
        # convert to number coordinate
        if x == 'a':
            self.player_input = int(str('1') + str(y))
        elif x  == 'b':
            self.player_input = int(str('2') + str(y))
        elif x  == 'c':
            self.player_input = int(str('3') + str(y))
        elif x  == 'd':
            self.player_input = int(str('4') + str(y))
        elif x  == 'e':
            self.player_input = int(str('5') + str(y))
        
    # Meehir    
    def wind_strength(self):
        """Determines the direction at which the wind is occuring.
        
        Return:
            wind strength which consists of direction
        """
        # list of potential directions
        direction = ['North', 'South', 'East', 'West']
        
        # random wind direction
        self.wind = random.choice(direction)
        
    # Meehir
    def validate_shot(self):
        """Determines distance from bullseye.

        Return:
            final coordinate distance from bullseye
        """
        # unpack final_coordinate as a string
        f,l = str(self.final_coordinate)
        
        if f == '1':
            self.final_coordinate = (str('A') + str(l))
        elif f == '2':
            self.final_coordinate = (str('B') + str(l))
        elif f  == '3':
            self.final_coordinate = (str('C') + str(l))
        elif f == '4':
            self.final_coordinate = (str('D') + str(l))
        else:
            self.final_coordinate = (str('E') + str(l))
        
        return self.final_coordinate
            
            
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
        
        
        letters = ['a','b','c','d','e']
        nums = ['1','2','3','4','5']
        rand_let = random.choice(letters)
        rand_num = random.choice(nums)
        computer_selected = rand_let + rand_num
        
        # unpack x and y from computer input
        # sets the selected_coordinate as an int
        if x in computer_selected == 'a':
            self.selected_coordinate = int(str('1') + str(y))
        elif x in computer_selected == 'b':
            self.selected_coordinate = int(str('2') + str(y))
        elif x in computer_selected == 'c':
            self.selected_coordinate = int(str('3') + str(y))
        elif x in computer_selected == 'd':
            self.selected_coordinate = int(str('4') + str(y))
        else:
            self.selected_coordinate = int(str('5') + str(y))
        
        print (f'Coordinate selected: ,{computer_selected}')
    

def game_over():
    """Game is over and determines the winner. 
    
    Return:
        boolean: false if game is not over true if game is over
    """
    player = HumanPlayer(0, "Player 1")
    #May need a function to determine winner 
    #How do I call score_per_game dict from here
    #best_score = max(player.score_per_game, key=player.score_per_game.get)
    #best_score = player.score_per_game.sort(key=lambda x: )
   
    
    if round == 3: 
        print(f"The winner is: {player.name} with a total score of: \
            {player.__iadd__()}")
        print()
        return True
    else:
        return False
    # use f-strings to display the name and total score over all 3 rounds
    # use custom list sorting to list best performing rounds by score

def winner(player):    pass

    
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
    