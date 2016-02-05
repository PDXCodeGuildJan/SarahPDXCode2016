""" Defines the Creature class, the base class of all living things in our game."""

class Creature:

	#these are (const) variables, globals inside of the class 
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONC = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"


	def __init__(self):
	#this is where we put the global arguments 

		self.name = ""
		self.state = NORMAL
		self.health = 20
		self.max_health = 20
		self.attack_points = 2
		self.weapon = None
		self.special_abilities = {}
		self.stats = {}
		


	def attack(self):

		pass

	def heal(self, amount):

		pass

	def defend(self, amount):

		pass

	def take_damage(self,damage):

		pass

	def change_weapon(self,new_weapon):

		pass 

	def change_state(self, new_state):

		pass 

