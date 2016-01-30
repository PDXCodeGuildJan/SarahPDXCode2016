""" A computer version of the game Angry Dice """

__author__ = "Sarah Fellows"


from random import randint 

def main():
	angry_instance = Angry_D() # 
	angry_instance.play_game()
	angry_instance.roll_dice()

	

class Angry_D: 
	""" Defines the variables and methods needed to play the game """

	def __init__(self):
	#this is where we need to put the global arguements 

		self.current_stage = 1
		self.current_goal = {1:[1,2], 2:["ANGRY",4], 3: [5,6]}
		self.player_name = ""
		self.die_1 = Die([1,2,"ANGRY",4,5,6])
		self.die_2 = Die([1,2,"ANGRY",4,5,6]) #Dice objects

	def play_game(self):
		"""Has the user play the game of Angry Dice. Starts the game,
			and loops through the game flow until they either win or
			quit."""

		print("Welcome to Angry Dice, the game that makes you so angry! If you get too angry and need to exit, please hit (E).")
		
		self.get_player_name()



	def get_player_name(self):
		""" Asking for player name and updating it in the game. """

		self.player_name = input("What is your name? ")


	def roll_dice(self):
		""" Rolls any dice not locked. """
		
		if not self.die_1.locked: #if the die is not locked then roll it 
			self.die_1.roll()

		if not self.die_2.locked:
			self.die_2.roll()

		print(self.die_1)
		print(self.die_2)	


	def check_angry(self):
		""" Defines method to check dice to see if both qualify as angry dice. """
		
		if self.die_1.value != 2:
			return 
		if self.die_2.value != 2: 
			return

		# If the code gets to here, we know they are angry
		self.current_stage = 1


	def win_round(self):
		""" Defines the method to check dice to see if both qualify as matching for winning round. """
		
		if self.die_1.value != self.current_goal

	def player_choice(self):
		""" Defines the method to allow player to hold one dice, roll one dice or to roll both die again."""
		pass 

	def evaluate_hold(self): 
		""" Defines the method to check to see the player is holding the correct die for their current stage."""
		pass	

	def advance_round(self):
		""" Defines the method that advances player to the next stage of the game """
		pass 


class Die(): 
	""" Defines the dice object """

	def __init__(self, sides):
		""" This stores the dice info."""
		self.sides = sides #Do I have to ask how many sides we need? 
		self.value = 0 #this starts the value of the dice at 1 

		self.locked = False 


	def __str__(self):
		"""Creates information to display side value"""
		
		return self.sides[self.value]



	def roll(self):
		""" Updating the value of the rolled dice"""
		self.value = randint(0, len(self.sides)-1)
		# Self.value is the randomization of the list 0 to the length of



if __name__ == '__main__':
	main()