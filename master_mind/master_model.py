""" A computer version the game of Mastermind """

__author__ = "Sarah Fellows"

class MasterModel:
""" This defines all the data that is changed and manipulated during the game """
    
    def __init__(self):
        self.guess_num = 1 #this is the stages of the game 
        self.goal = [] #computer generated random goal 
        self.guesses = Guess() #appended list of all guesses made across whole game 


class Guess:
    """ stores history of guesss made accross the whole game - what has been presneted and what has been guessed 
        - the player pegs and key pegs """
    
    def __init__(self):
        self.player_peg = [] #stores the string the player guesses 
        self.key_peg = [] #stores the computers response/suggestions for the next round

class PlayerPeg:
    """ Defines what the Player Pegs are"""

    def __init__(self, color):
        """ Stores the player peg properties """
        self.color = color

class KeyPeg: 
    """ Defines the Key Pegs returned from the evalation of player pegs choices """
    
    SMALL_BLACK = "small_black"
    SMALL_WHITE = "small_white"

    def __init__(self)