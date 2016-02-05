from random import randint

sides = Die([1,2.3,4,5,6])

class Die():
"""Defines a die object"""

	def __init__(self, sides):
		""" This stores the dice information. Initializes the dice. Defines what the die are."""
		self.current_index = 0 
		self.possible_values = sides #self.sides 

	def __str__(self):
		""" Creates information to display the side value and return a string """

		temp = "["
		temp += str(self.possible_values[self.current_index])
		temp += "]"

		return temp[self.current_index]

	def roll(self):

		self.current_index = randint(0, len(self.possible_values)-1)
