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
    def __init__(self, name): #Khaliil
        """Function that will initialize the objects that were represented in
           the attributes.
           
        Args:
            name (str): user inputted name
        """
        self.scores = {0:0}
        self.name = name
        self.wind_strength()
        
    #Uses f-strings to print out relevant information regarding the game
    def round(self): #Khaliil
        """Initiates one round of the game.
        Side Effects:
            prints to the terminal
        """
        rounds = 0 
        while self.game_over(rounds) == False:
            # Displays current round and current score at beginning of round 
            print(f"The current score is {self.total_score()}") 
            print(f"Round {rounds} of 3")
            rounds += 1
            
            # Displays current player's turn 
            print(f"{self.name}, it is your turn")

           
            self.wind_strength()
             # Display wind strength
            print(f"The current wind direction is {self.wind} ") 
            self.turn()
            self.coordinates()
            self.score(rounds)
        return self.scores
    
    #uses magic methods to compare the values in dictionaries 
    def __lt__(self, other): #Brice 
        """Method used to compare the two dictionaries of values in the game

        Args:
            other (dict): dictionary used to store scores from the game

        Returns:
            Boolean: Returns true or false if current scores is less than
                     the other's scores.
        """
        return self.scores.values < other.scores.values
      
    #Helper function
    def total_score(self): #Brice
        """Method used to calculate the total score from the values in the 
           dictionaries  

        Returns:
            Integer: total score from the values
        """
        return sum(self.scores.values())
    
    #uses magic methods to compare the values in dictionaries
    def __eq__(self, other): #Brice
        """Method used to compare the two dictionaries of values in the game

        Args:
            other (dict): dictionary used to store scores from the game

        Returns:
            Boolean: Returns true or false if current scores is equal than
                     the other's scores.
        """ 
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

        Args:
            rounds (_type_): _description_
         
        Side Effects:
            adds new scores to the dictionary

        """
        # scores in each round will be stored in a dictionary with the rounds 
        # being the keys and the scores as the values.
        # determine score using conditional expressions, 
        # if _ unit from the bullseye then assign _ points
        

        # 11 21 31 41 51        A1 B1 C1 D1 E1
        # 12 22 32 42 52        A2 B2 C2 D2 E2
        # 13 23 33 43 52        A3 B3 C3 D3 E3
        # 14 24 34 44 54        A4 B4 C4 D4 E4
        # 15 25 35 45 55        A5 B5 C5 D5 E5
        
        if self.final_coordinate == 33:
            points = 10
        elif self.final_coordinate == 22 or self.final_coordinate == 32 \
            or self.final_coordinate == 42 or self.final_coordinate == 23 \
            or self.final_coordinate == 43 or self.final_coordinate == 24 \
            or self.final_coordinate == 34 or self.final_coordinate == 44:
            points = 5
        else:
            points = 1
        
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
    
    # use f-strings to display the name and total score over all 3 rounds
    # use custom list sorting to list best performing rounds by score
    def game_over(self, rounds): #Brice
        """Game is over and determines the winner. 
        
        Return:
            boolean: false if game is not over true if game is over
        """
    
        highest_score = max(self.scores.values())
        
        if rounds == 3: 
            print(f"Total score for {self.name} is {self.total_score()}")
            print(f"{self.name} highest score from 3 rounds was {highest_score} \n \
                  Here is their score chart for the game: ")
            self.scores.pop(0)
            for key, value in sorted(self.scores.items(), key = lambda x: x[1],\
                reverse = True):
                print(key, value)
                
            return True
        else:
            return False
        
class ComputerPlayer(HumanPlayer):
    # inherits all the methods from the HumanPlayer class
    # Overrides some functions from the HumanPlayer class  
    """Represents a computer player 
    Attributes:
        cname (str): name for computer player
    """
    
    # Optional parameter for computer name 
    def __init__(self, cname): #Brice
        """Function that will initialize the objects that were represented in
           the attributes.
        """
        # Uses super to call the init method from the human class
        super().__init__(cname)
        self.player_input = 0
        
        
    def turn(self): #Raeen
        """Overides human and generates random coordinates within bounds 
        to shoot.
        
        Side Effects:
            prints the coordinates the computer selected
            
            selected_computer_coordinate is changed from a string to an int.
            
            final_coordinate is instantiated with the same value as the computer_selected attribute.
        """         
        # Overrides the turn method in the human class since computer turn 
        # randomly generates a coordinate to shoot
        
        letters = ['a','b','c','d','e']
        nums = ['1','2','3','4','5']
        rand_let = random.choice(letters)
        rand_num = random.choice(nums)
        computer_selected = rand_let + rand_num
        
        # unpack x and y from computer input
        x = rand_let
        y = rand_num
        
        # sets the selected_coordinate as an int
        if x == 'a':
            self.selected_computer_coordinate = int(str('1') + str(y))
        elif x == 'b':
            self.selected_computer_coordinate = int(str('2') + str(y))
        elif x == 'c':
            self.selected_computer_coordinate = int(str('3') + str(y))
        elif x == 'd':
            self.selected_computer_coordinate = int(str('4') + str(y))
        elif x == 'e':
            self.selected_computer_coordinate = int(str('5') + str(y))
        
        self.final_coordinate = computer_selected
        print (f'Coordinate selected: ,{computer_selected}')
    
    #Overides HumanPlayer's coordinate method slightly to fit computer's 
    #random coordinate generation.    
    def coordinates(self): #Brice
        """Coordinate is determined based on relative position of shot to center
        and accounts wind interference.
        
        Side effects: 
            final_coordinate attribute is set to the winds effect on the 
            selected_computer_coordinate attribute.
        """ 
        # the final coordinate depends on the random wind direction's affect on 
        # the computer's selected coordinate. 
        if self.wind == 'North':
            self.final_coordinate = self.selected_computer_coordinate + 1
        elif self.wind == 'South':
            self.final_coordinate = self.selected_computer_coordinate - 1
        elif self.wind == 'East':
            self.final_coordinate = self.selected_computer_coordinate + 10
        elif self.wind == 'West':
            self.final_coordinate = self.selected_computer_coordinate - 10
            
def main(human, computer):#Khaliil
    """Plays one round of the archery game and calls necessary 
    methods/functions.
    Args:
        human (str): name of human player
        computer(str): name of computer player
    """
    play_again = "y"

    while play_again == "y": 
        human_player = HumanPlayer(human)
        human_score = human_player.round()
        computer = ComputerPlayer(computer)
        computer_score = computer.round()

        #Uses conditional expressions to evaluate the result of the comparison
        #of scores between the computer and human player. 
        if human_player.total_score() > computer.total_score():
            print(f"{human_player.name} wins")
        elif human_player.total_score() < computer.total_score():
            print("Computer wins!")
        else:
            print("It's a tie!")
        play_again = input("Would you like to play again?")

        if play_again != "y":
            break

# Argument parser in order to use command line arguments 
# (player name and desired target) 
def parse_args(arglist):#Brice
    """Parse command line arguments.
    
    Expect three mandatory arguments:
        - str: name of player
        - str: name of second player/computer player
        - str: desired position on target
    
    Args:
        arglist (list of str): arguments from command line
    
    Returns:
        namespace: parsed arguments
    """ 
    parser = argparse.ArgumentParser()
    parser.add_argument("player1", help= "Name of the first player")
    parser.add_argument("computer", help= "Name of the computer player")
    return parser.parse_args(arglist)
 
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1, args.computer)