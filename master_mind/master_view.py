""" A computer version the game of Mastermind """

__author__ = "Sarah Fellows"
   

class MasterView:
    """ This class displays the information given to it from the controller"""

    def show_rules(self):
        """This method displays the welcome and the rules of the game before 
            the game starts"""
        
        print ("Welcome to Master Mind!")

        self.get_player_name()

        print ("Here are the rules")

    def get_player_name(self): 
        """ Asking for player name and updating it in the game"""

        self.player_name = input("Please tell me your name....")
        print("Hi {0}! Here are the rules: ").format(self.player_name)

    def show_player_peg(self):
        """This method shows the player's guesses throughout the game"""
        pass

    def show_key_peg(self):
        """ This method shows the computer suggestions (small black and white 
            pegs) to allow player to get closer to the computer generated 
            goal"""
        pass

    def promt_user(self):
        """ This method prompts the user to make a guess at what they 
            think the end goal is"""
        pass

    def win(self):
        """This method pops up when the use wins the game""" 
        pass

    def game_over(self):
        """This method pops up when the user looses all 10 rounds""" 
        pass 



