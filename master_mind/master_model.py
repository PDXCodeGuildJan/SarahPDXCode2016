""" A computer version the game of Mastermind """

__author__ = "Sarah Fellows"

class MasterModel:
""" This defines all the data that is changed and manipulated during the game"""
    
    def __init__(self):
    #this is where we put the global arguments for the game 

        self.guess_num = 1 #this is the stages of the game 
        self.goal = [] #computer generated random goal 
        self.guesses = (Guess) #appended list of all guesses made across whole game 
        self.peg_colors = ["Yellow", "Red", "Blue", "Green", "Black", "White"]
        self.key_list = Guess.key


class Guess:
    """ stores history of guesss made accross the whole game - what has been 
        presneted and what has been guessed  - the player pegs and key pegs """

    #This needs to take in the guess from the player as well we the record of  
    #computer generated suggests (key pegs)

    def __init__(self):
        self.player_peg = [] #stores the current player guess
        self.key_peg = [] #stores the computers response/suggestions for the next round

class PlayerPeg:
    """ Defines the six color player Pegs"""

    # def __init__(self, color):
    #     """ Stores the player peg properties. Initalized the pegs and colors """
    #     self.color = color
    #     self.index = 0 #Starts the value of the string at 0
    #     self.locked = False 

    # def __str__(self):
    #     """Creates the information to display the colors and returns it in a 
    #         string"""

    #         temp = "("
    #         temp += str(self.color[self.index])
    #         temp += ")"


class KeyPeg: 
    """ Defines the Key Pegs returned from the evalation of player pegs 
        choices """

    #Takes in the player's guess and returns the key pegs based on choice
    
    #Create the key pegs 
    SMALL_BLACK = "small_black"
    SMALL_WHITE = "small_white"

    def __init__(self)