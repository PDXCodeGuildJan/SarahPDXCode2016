""" A computer version of the game Angry Dice """

__author__ = "Sarah Fellows"


from random import randint 

def main():

	game_instance = Angry_D()
	game_instance.play_game()

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

		print("\n\nWelcome to Angry Dice, the game that makes you so angry!\n")
		
		self.get_player_name()

		self.rules()

		#This while loop needs to come after the welcome so it doesnt repeat itself.
		while self.current_stage < 4:

			#Roll their first die
			self.roll_dice()

			#Once the dice is rolled, check to see if it meets the check_angry standards 
			if self.check_angry():
				#this keeps it looping but pushes it to the top of the loop right now 
				continue

			#Check if player wins the round and advance round 
			if self.win_round():
				continue

			self.player_choice()

			self.evaluate_lock()


	def get_player_name(self):
		""" Asking for player name and updating it in the game. """

		self.player_name = input("\nPlease tell me your name... ")
		print("\nHi {0}! Lets Play! If you get too angry and need to exit, please hit 'control and C' at the same time." .format(self.player_name))


	def rules(self):

		player_rule_answer = input("\n        Would you like to see the rules? Type 'Y' for yes or anything else for no.")

		if player_rule_answer.upper() == "Y":
			print("\n~~~~~~~~~~~Here are the rules:~~~~~~~~~~~\n\n------The Battle------\nPlayers roll their dice at the **same time**,",
				"trying to get from 1 to 6 the fastest.\nThe first to do so wins! \n\n------The Details------\n",
				"Stage 1, then Stage 2, then Stage 3. When each Stage is complete, the player' must declare it out loud.", 
				"Each player needs two Angry Dice. Players roll their dice, looking to complete.\n\n",
				"------Stage 1--------\nOne die showing 1 pip, another showing 2 pips. \n\n--------Stage 2--------\n One die showing the Angry face",
				"(which represents a 3), another showing 4 pips.\n\n--------Stage 3--------\nOne die showing 5 pips, another showing 6 pips.\n\n",
				"\nPlayers do not have to perfectly roll each Stage;\nif a die shows one face in a set, that die is locked (left aside) and",
				"the player now rolls the other die to complete the set.\n\nEXCEPTION: The 6 die face may never be locked!",
				"\n\n-------The Anger-------\nIf the dice ever show both Angry Faces, the player must START OVER from **Stage 1**.", 
				"\n\n-------The Victory-------\nThe first player to race through all Stages to reach Stage 3 and announces",
				"'GET ANGRY!' is declared the victor!")

		input("\n\n\nPress ENTER to start the game and to roll the dice!")

	def roll_dice(self):
		""" Rolls any dice not locked. """
		
		if not self.die_1.locked: #if the die is not locked then roll it 
			self.die_1.roll()

		if not self.die_2.locked:
			self.die_2.roll()

		print("\n\n Here are the die you rolled:")
		print(self.die_1)
		print(self.die_2)	

	def check_angry(self):
		""" Defines method to check dice to see if both qualify as angry dice. """
		
		if self.die_1.index == 2 and self.die_2.index == 2:
			self.current_stage = 1
			print("(╯︵╰,),", 
				"You rolled to Angry Dice! You have been thrown back to the Stage 1, your new goal is die 1 and 2.",
				"Try not to be angry!",
				"(╯︵╰,)")
			return True

		else:
			return False 


		#This is another way to code it below: 
		# if self.die_1.value != 2:
		# 	return False
		# if self.die_2.value != 2: 
		# 	return False
  
		# # If the code gets to here, we know they are angry
		# self.current_stage = 1


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
						print("\n\n¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸",
							"\nᕕ( ᐛ )ᕗ Congratulations, you won! Announce 'GET ANGRY! to your competition ᕕ( ᐛ )ᕗ",
							"\n¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩¸¸♪·¯·♫¸¸¸¸♬·¯·♩")
						exit()

					else:
						self.current_stage += 1
						print("\n\n..:*~*:._.:*~*:._.:**:._.:**:._.:*~*:CONGRATULATIONS:*~*:._.:**:._.:**:._.:*~*:._.:*~*:..\n\n",
							"You have advanced to the next Stage! BE SURE TO TELL YOUR PARTNER AS LOUD AS YOU CAN!!!", 
							"\n\n*~*:._.:**:._.:*~*:._.:*~*:*~*:._.:**:._.:**:._.:*~*:._.:**:._.:*~*:._.:**:._.:*~*:._.:*~*:\n\n")
						return True
						#we need to know if we changed rounds or not 

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
			entree = input("Would you like to reroll (a)ll of the die, just the (t)op die or just the (b)ottom die?")

			#Choices:
			# Reroll both
			if entree.lower() == "a":
				invalid_choice = False

			#Lock/Hold die_1, roll die_2
			elif entree.lower() == "t":
				self.die_2.locked = True
				invalid_choice = False

			elif entree.lower() == "b":
			#Lock/Hold die_2, roll die_1 
				self.die_1.locked = True
				invalid_choice = False

			elif entree.upper() == "E":
				print("We are so sorry to see you go, I was looing forward to you getting so ANGRY!!!")
				exit()

			else:
				print("I do not understand your choice.")


	def evaluate_lock(self): 
		""" Defines the method to check to see the player is holding the correct die for their current stage."""
		#This function needs to take in the players choice and make sure it matched the round they on 

		current_goal = self.stage_goal[self.current_stage]
		print("\n\t»»---------------------► Remember, your current goal is:", current_goal)

		# check both dice to see if they are locked, and if so, validly locked
		for die in [self.die_1, self.die_2]:
			#see if locked dice matches current goals 
			if die.locked:

				#if the rolled value matches the current goal value
				if die.sides[die.index] in current_goal:	

					# Make sure it isn't a 6, warn them if it is
					if die.sides[die.index] == 6:

	  					#give them a warning because they tried to lock in a 6 
	  					print("\n********Ops! You forgot, you can't lock in a 6********")
	  					die.locked = False

				else:
					
					#if it doesn't match, print a warning, don't allow player to lock die, ask if they would like to reroll
					print("\n\n\n\t********OPS! The die you locked doesn't match your current round's goals therefore you can't lock this die.********", 
						"\n\t********We will reroll both die now.********")
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

		#Below is the code what we did before making the dice pretty. 
		# temp = "["
		# temp += str(self.sides[self.index])
		# temp += "]"

		pretty_dice = [
		
		"""
+-------+
|       |
|   1   |
|       |
+-------+""",

"""
+-------+
|     2 |
|       |
| 2     |
+-------+""",
"""
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",
"""
+-------+
| 4   4 |
|       |
| 4   4 |
+-------+""",
"""
+-------+
| 5   5 |
|   5   |
| 5   5 |
+-------+""",
"""
+-------+
| 6   6 |
| 6   6 |
| 6   6 |
+-------+"""
]

		# we want to return a string that looks like a die 
		return pretty_dice[self.index]

	def roll(self):
		""" Updating the value of the rolled dice by choosing one of the sides"""
		self.index = randint(0, len(self.sides)-1)
		# Because the length of the list is 6 but because the list starts at 0, we have to -1 to get the actual length 


# def test_evaluate_lock():
# 	angry_instance = Angry_D()
# 	angry_instance.die_1.index = 0
# 	angry_instance.die_2.index = 0
# 	angry_instance.die_1.locked = True
# 	angry_instance.die_2.locked = True
# 	angry_instance.current_stage = 1
# 	print("Die 1 is {}, die 2 is {}".format(angry_instance.die_1.locked, angry_instance.die_2.locked))
# 	angry_instance.evaluate_lock()
# 	print("Die 1 is {}, die 2 is {}".format(angry_instance.die_1.locked, angry_instance.die_2.locked))



# def test_player_choice():
# 	angry_instance = Angry_D()
# 	angry_instance.die_1.index = 1
# 	angry_instance.die_2.index = 1
# 	print("Die 1 is {}, die 2 is {}".format(angry_instance.die_1.locked, angry_instance.die_2.locked))
# 	angry_instance.player_choice()
# 	print("Die 1 is {}, die 2 is {}".format(angry_instance.die_1.locked, angry_instance.die_2.locked))


# def test_roll_and_play():
# 	angry_instance = Angry_D() 
# 	angry_instance.play_game()
# 	angry_instance.roll_dice()


# def test_advancing_rounds():
# 	angry_instance = Angry_D() 
# 	angry_instance.current_stage = 1 
# 	angry_instance.die_1.index = 0
# 	angry_instance.die_2.index = 1
# 	angry_instance.win_round()


if __name__ == '__main__':
	main()

