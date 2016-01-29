""" A computer version of the game Angry Dice """

__author__ = "Sarah Fellows"


from random import randint 

def main():


class Angry_D: 
""" Defines the variables and methods needed to play the game """

	def __init__(self, player_name):
	#this is where we need to put the global arguements 

		self.current_stage: 1
		self.current_goal: []
		self.player_name: ""
		self.die_1: {Die} #Should/can we make the dice a dictonary? Look into further. 
		self.die_2: {Die}

		pass

	def roll_dice(self, die_1, die_2):
	""" Rolls both of the dice """
		pass

	def check_angry(self, die_1, die_2):
	""" Defines method to check dice to see if both qualify as angry dice. """
		pass 

	def win_round(self, current_stage):
	""" Defines the method to check dice to see if both qualify as matching for winning round. """
		pass 

	def player_choice(self, die_1, die_2):
	""" Defines the method to allow player to hold one dice, roll one dice or to roll both die again."""
		pass 

	def evaluate_hold(self, die_1, die_2): 
	""" Defines the method to check to see the player is holding the correct die for their current stage."""
		pass	

	def advance_round(current_stage):
	""" Defines the method that advances player to the next stage of the game """
		pass 


class Die: 
""" Defines the object that describes the dice """





















if __name__ == '__main__':
	main()