"""Implement an MVC Mastermind game for one player. This file is the controller."""

__author__ = "Ron Shafii and Sarah Fellows"


from mastermind_model import * #imports all classes
from mastermind_view import *
import random



class MasterMind:


	def __init__(self):
		self.model = MasterModel()
		self.view = MasterView()
		



	def generate_goal(self):
		"""create 4 randomly generated colored pegs to establish the goal of the game."""#need to return to fix use of peg colors
		goal = []
		temp_list = [PlayerPeg.RED, PlayerPeg.GREEN, PlayerPeg.BLUE, PlayerPeg.YELLOW, PlayerPeg.BLACK, PlayerPeg.WHITE]

		for x in range(4):
			player_peg = PlayerPeg(random.choice(temp_list))
			goal.append(player_peg)

		self.model.goal = goal 
		



	def play_game(self):
		"""plays the mastermind game"""

		self.model.guess_num = 10


		#Show the game rules and objectives
		self.view.show_rules()

		# Generate the Goal
		self.generate_goal()

		#Starts the counter for guesses left 
		while self.model.guess_num <= 10: 

			#prompt the user to enter 4 colors
			self.store_player_pegs()

			#check if the user won 
			self.check_win()

			#Evaluates the player's guesses and produces key pegs from evaluation
			self.eval_player_guess()

			#creates a history of guesses by adding the current guess to the histort list 
			self.model.guesses.append(self.model.current_guess)

			self.view.show_board(self.model.guesses)

			#display to the user the number of guesses left before they lose the game
			#if the number of guesses == 0 then display they lost the game.

			#loop back to prompt the user to enter 4 colors 


	def store_player_pegs(self):
		"""Call prompt_user to obtain player pegs. Turn prompt_user() string into a Guess object and store it in the guesses[Guess] list"""
		# 
		prompt_user_results = self.view.prompt_user()

		#create a temp list
		temp_list = []

		#turn a character into a peg
		for char in prompt_user_results:
			if char == "Y":
				peg = PlayerPeg(PlayerPeg.YELLOW)
			elif char == "B":
				peg = PlayerPeg(PlayerPeg.BLUE)
			elif char == "G":
				peg = PlayerPeg(PlayerPeg.GREEN)
			elif char == "R":
				peg = PlayerPeg(PlayerPeg.RED)
			elif char == "K":
				peg = PlayerPeg(PlayerPeg.BLACK)
			elif char == "W":
				peg = PlayerPeg(PlayerPeg.WHITE)
			temp_list.append(peg)

		#create a Guess object, move the results stored in temp_list and convert them to an object then store them as a list in guesses
		temp_object = Guess() #creating an object of the Guess class
		temp_object.player_pegs = temp_list #change the temp_list to a Guess object 
		self.model.current_guess = temp_object #storing the objects as a list in MasterModel-guesses

		
	def check_win(self):
		"""checks to see if the player's guess (self.model.current_guess) exactly matches the 
		4 computer generated pegs (self.model.goal). """
		
		#checks the player's current guess to see if it's an exact match with goal
		goal = self.model.goal
		current_guess = self.model.current_guess.player_pegs

		if goal == current_guess:
			return "You've Won!"


	def eval_player_guess(self):

		"""Evaluates the players peg guesses against the goal and returns key pegs """

		#if the user didn't win evaluate the player's peg colors against the computer_peg colors
		#if player colors match then evaluate if any of the player's pegs position match the computer's peg positions
		#return the appropriate position and color matches to the player
		 
		#Results are stored by class Guess in the model.
		
		goal = self.model.goal[:]
		current_guess = self.model.current_guess.player_pegs[:]
		peg_list = []

		#First for loop checks for exact match (color and position) and replaces each match with an empty string so duplations won't be made in future loop
		for i in range(4):

			#if an exact match exists between current_guess and goal exists
			if current_guess[i].color == goal[i].color: 
				#create a variable that holds a small_black key_peg 
				temp_peg = KeyPeg(KeyPeg.SMALL_BLACK) 
				#add the small_black peg to the peg_list that will be returned to the player
				peg_list.append(temp_peg)

				#Testing print function to be removed later - wanting to show black key pegs 
				#print("Adding black pegs because of", goal[i].color)
				
				#insert an empty string to act as a place holder for the matched values in the current_guess list and the goal_list
				#removes the matched colors/position in guess 
				current_guess.pop(i) 
				#replaces what was taken out with .pop and inserts an empty string in its place
				current_guess.insert(i, "")
				#need to do the same with the goal to avoid dulplicates 
				goal.pop(i)
				goal.insert(i, "")

				
				 
		#compare current objects in remaining current_guess list against objects in remaining goal_list for color match only and return a white peg 
		for i in range(4): 
			#As long as the object isn't an empty string... 
			if current_guess[i] != "": 
			 	
			 	#Start second loop to iterate through guess list after a match occurs 
			 	for k in range(4):
			 		#Ignore any empty strings in the list
			 		if goal[k] != "":
			 			#if remaining colors in the guess list matches remaining colors in the goal list
				 		if current_guess[i].color == goal[k].color: 
				 			#create a white peg if remaining colors match 
						 	temp_peg2 = KeyPeg(KeyPeg.SMALL_WHITE)
						 	peg_list.append(temp_peg2)

						 	#used for testing only
						 	#print("Adding white pegs because of", goal[k].color)

						 	#replaces matches with emprty string to avoid duplicates 
						 	goal.pop(k)
						 	goal.insert(k, "")

						 	break #we want to stop going through the loop once we find one to avoid dups, not continue  

		#we need to store peg list with the history of guesses
		self.model.current_guess.key_pegs = peg_list

		#print(len(peg_list)) #Need to get rid of this eventually 




def test_eval_peg_color():
	test_instance = MasterMind() #new object of the game
	test_instance.generate_goal() #generated a goal 
	for peg in test_instance.model.goal:
		print(peg)
	test_instance.store_player_pegs() #prompts for the guess 

	test_instance.eval_peg_color()


def test():
	#testing the random color generator
	test_object = MasterMind()
	temp_list = test_object.generate_goal()
	for peg in temp_list:
		print(peg.color)


def main():

	test_object = MasterMind()
	test_object.play_game()

if __name__ == '__main__':
	main()
	#test()
	#test_eval_peg_color()


