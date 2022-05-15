import argparse
from optparse import Values
import sys
import random
from functools import total_ordering

score_per_round = dict()

@total_ordering
class HumanPlayer():
    """Represents a Human player
    
    Attributes:
        scores (dict): score of player
        name(str): Name of current player 
    """
    # utilizes optional parameters of name
    def __init__(self, name = 'Player 1'): #KHALIIL
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            score(integer): score of player
            name (str): user inputted name
        """
        self.scores = {}
        self.name = name
    
    def round(self, rounds): #Khaliil
        """Initiates one round of the game.
        """
        rounds = 0 
        while self.game_over(rounds) == False:
            # in the begining of each round anounce the current round, and display current score 
            print(f"The current score is {self.score()}") 
            print(f"Round {rounds} of 3")
            # there should be a total of three rounds, and the first player to win 2 rounds wins, but as long as the game is not over keep initiating
            rounds += 1
            # announce whose turn it is
            print(f"{self.name}, it is your turn")
            # display wind strength
            print(f"The current wind direction is {self.wind_strength} ")
        
    def __lt__(self, other): #Brice
        return self.scores.values < other.scores.values
    #compares scores based on self.score
    #compute the sum of the values of self.score, use sum function
    #dictionaries has a .value function
    
    #Helper function for the total score
    def total_score(self): #Brice 
        return sum(self.scores.values())
    
    def __eq__(self, other): #Brice
        return self.scores.values == other.scores.values
    
    # Meehir
    def coordinates(self):
        """Coordinate is determined based on relative position of shot to center and 
        accounts wind interference.
        
        Side effects: 
            final_coordinate attribute is set to the winds effect on the player_input attribute.
        """ 
        # the final coordinate depends on the random wind direction's affect on the player_input
        if self.wind == 'North':
            self.final_coordinate = self.player_input + 1
        elif self.wind == 'South':
            self.final_coordinate = self.player_input - 1
        elif self.wind == 'East':
            self.final_coordinate = self.player_input + 10
        elif self.wind == 'West':
            self.final_coordinate = self.player_input - 10
            
    def score(self, rounds): #Raeen
        """Score taken from coordinate shot landed on. Score calls validate_shot
        to distribute points based on where shot landed. 
        """
        # scores in each round will be stored in a dictionary with the rounds 
        # being the keys and the scores as the values.
        # determine score using conditional expressions, 
        # if _ unit from the bullseye then assign _ points
        
        
        if self.validate_shot(self.player_input) == 0:
            points = 10
        elif self.validate_shot(self.player_input) == 1:
            points = 5
        elif self.validate_shot(self.player_input) == 2:
            points = 3
        else:
            points = 0
        
        self.scores[rounds] = points
        
    # Meehir           
    def turn(self):
        """Prompts player for desired coordinates and makes sure inputted 
        coordinates are valid.
        
        Side effects:
            prints message prompting user to console and empty lines for formatting.
            
            player_input attribute is set to user input and changed to lowercase.
            
            player_input is changed from a string to an int.
            
            final_coordinate is instantiated with the same value as the player_input attribute.
        """
        # use sequence unpacking to access the x (letter) and y (number) to interpret desired coordinate
        # e.g., c3 would unpack to x = c and y = 3 and ultimately x = 3 and y = 3
        
        # possible inputs given wind direction
        N = ['a1', 'a2', 'a3', 'a4' 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4']
        S = ['a2', 'a3', 'a4', 'a5', 'b2', 'b3', 'b4', 'b5', 'c2', 'c3', 'c4', 'c5', 'd2', 'd3', 'd4', 'd5', 'e2', 'e3', 'e4', 'e5']
        E = ['a1', 'a2', 'a3', 'a4', 'a5' , 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5']
        W = ['b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']
        
        # prompts users for coordinate with restrictions applied and makes sure user input is valid
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
        
        self.final_coordinate = self.player_input
        
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
        """randomly generates a wind direction from a list of North,
        South, East, and West.
        
        Side effects: 
            creates wind attribute and sets it to a random cardinal direction.
        """
        # list of potential directions
        direction = ['North', 'South', 'East', 'West']
        
        # random wind direction
        self.wind = random.choice(direction)
        
    # Meehir
    def validate_shot(self):
        """unpacks final_coordinate attribute and changes it from an 
        int to a string.

        Side effects:
            final_coordinate attribute is changed from an int to a string.
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

        #Is the distance to bullseye always 2? 
        self.distance_to_bullseye = 2
        
        return self.distance_to_bullseye
    
    def game_over(self, rounds): #Brice
        """Game is over and determines the winner. 
        
        Return:
            boolean: false if game is not over true if game is over
        """
        #player = HumanPlayer(0, "Player 1")
        #May need a function to determine winner 
        #How do I call score_per_game dict from here
        #best_score = max(player.score_per_game, key=player.score_per_game.get)
        #best_score = player.score_per_game.sort(key=lambda x: )
    #Call total_Score
        score_chart = sorted(self.scores, key= lambda x: x[1], reverse = True)
        highest_score = max(self.scores, key = self.scores.get)
        
        if rounds == 3: 
            print(f"The winner is: {self.name} with a total score of: "
                f"{self.total_score}")
            print("The winning player's highest score was {highest_score}" 
                  f"Here is their score chart for the game: {score_chart}")
            return True
        else:
            return False
        # use f-strings to display the name and total score over all 3 rounds
        # use custom list sorting to list best performing rounds by score
    

class ComputerPlayer(HumanPlayer):
    # inherits all the methods from the human class
    """Represents a computer player 

    Attributes:
        cname (str): name for computer player
    """
    
    # optional parameter for computer name 
    def __init__(self, cname = 'Computer'): #Brice
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        # uses super to call the init method from the human class
        super().__init__()
        
    def turn(self): #Raeen
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
    


#Don't think we need anymore
def winner(player):    
    pass

    
def main():#Khaliil
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
    