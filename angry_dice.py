""" A computer version of the game Angry Dice """

__author__ = "Sarah Fellows"


from random import randint 

def main():
	angry_instance = Angry_D() 
	angry_instance.play_game()
	angry_instance.roll_dice()

	angry_instance.current_stage = 1 
	angry_instance.die_1.index = 0
	angry_instance.die_2.index = 1

	angry_instance.win_round()

class Angry_D(): 
	""" Defines the variables and methods needed to play the game """

	def __init__(self):
	#this is where we need to put the global arguements 

		self.current_stage = 1
		self.stage_goal = {1:[1,2], 2:["ANGRY",4], 3: [5,6]}
		self.player_name = ""
		self.die_1 = Die([1,2,"ANGRY",4,5,6])
		self.die_2 = Die([1,2,"ANGRY",4,5,6]) #Dice objects

	def play_game(self):
		"""Has the user play the game of Angry Dice. Starts the game, and loops through the game flow until they either win or quit."""

		print("\nWelcome to Angry Dice, the game that makes you so angry!\nIf you get too angry and need to exit, please hit (E).")
		
		self.get_player_name()


	def get_player_name(self):
		""" Asking for player name and updating it in the game. """

		self.player_name = input("\nWhat is your name? ")
		print("\nHi {0}! Roll your dice now!" .format(self.player_name))


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
		print("You rolled to Angry Dice! You have been thrown back to the beginning. Try not to be angry! ")

	def win_round(self):
		""" Defines the method to check dice to see if both qualify as matching for winning round. """
		
		#Get current goal - for the first round, the current goal is equal to the stage goals current index 
		current_goal = self.stage_goal[self.current_stage]
		
		#See if goal is met 

		# If the die one roll matches any number in the stage goal,
		if self.die_1.sides[self.die_1.index] in current_goal: # same thing as list[index]
			 # then check the second die. if doesn't match, return to main. 
			if self.die_2.sides[self.die_2.index] in current_goal:

			#Only if the first die matches, check the second die to make sure is not the same number 
			#but instead the other stage goals index 
				if self.die_1.index != self.die_2.index:

					if self.current_stage == 3:
						print("Congratulations, you won! ")
						exit()

					else:
						self.current_stage += 1
						print("Congratulations! You have advanced to the next round!")

	def player_choice(self):
		""" Defines the method to allow player to hold one dice, roll one dice or to roll both die again."""
		
		# Unlock any currently locked dice
		self.die_1.locked = False
		self.die_2.locked = False

		#Make a temporary variable in order to be able to stop the while loop 
		invalid_choice = True

		#While the invalid choice 
		while invalid_choice:
			#this function needs to take in the already rolled dice, and give out what their choice
			#if self.die_1.value
			self.make_choice = input("Would you like to reroll the (T)op die or the (B)ottom die?")

			#Choices:
			# Reroll both
			if entree.lower() == "r":
				invalid_choice = False

			#Lock/Hold die_1, roll die_2
			elif entree.lower() == "t":
				self.die_2.locked = True
				invalid_choice = False

			elif entree.lower() == "b":
			#Lock/Hold die_2, roll die_1 
				self.die_1.locked = True
				invalid_choice = False

			else:
				print("I do not understand your choice.")


	def evaluate_lock(self): 
		""" Defines the method to check to see the player is holding the correct die for their current stage."""
		#This function needs to take in the players choice and make sure it matched the round they on 

		current_goal = self.stage_goal[self.current_stage]

		# check both dice to see if they are locked, and if so, validly locked
		for die in [self.die_1, self.die_2]:
			#see if locked dice matches current goals 
			if die.locked:

				#if the rolled value matches the current goal value
				if die.sides[die.index] in current_goal:	

					# Make sure it isn't a 6, warn them if it is
					if die.sides[die.index] == 6:

	  					#give them a warning because they tried to lock in a 6 
	  					print("Ops! You forgot, you can't lock in a 6.")
	  					die.locked = False

				else:
					
					#if it doesn't match, print a warning, don't allow player to lock die, ask if they would like to reroll
					print("The die you locked doesn't match your current round's goals therefore you can't lock this die.")
					die.locked = False 



class Die(): 
	""" Defines the dice object """

	def __init__(self, sides):
		""" This stores the dice info. Initalizes the dice and defines what the die are. """
		self.sides = sides #Do I have to ask how many sides we need? 
		self.index = 0 #this starts the value of the dice at 1 
		self.locked = False #this says that the self.locked function is false - therefore unlocked 

	def __str__(self):
		"""Creates information to display side value - return the string. """
		# __str__ built in function that overrides what Python was doing before, so it does what we tell it to instead 
		# we never print inside of this string unless we are debugging 

		temp = "["
		temp += str(self.sides[self.index])
		temp += "]"
		
		# we want to return a string that looks like a die 
		#return self.sides[self.value]
		return temp

	def roll(self):
		""" Updating the value of the rolled dice by choosing one of the sides"""
		self.index = randint(0, len(self.sides)-1)
		# Because the length of the list is 6 but because the list starts at 0, we have to -1 to get the actual length 


if __name__ == '__main__':
	main()