""" Defines the Creature class, the base class of all living things in our game."""

class Weapon:
	"""Weapon object that creatures can equip"""

	def __init__(self, atk_value): 
		self.base_damage = atk_value



class Creature:
	#When you forget the () after the class name, you are not creating a new one, you are calling a template - a 
	#reference to the actual written code that is the function

	#these are (const) variables, kind of like globals inside of the class, all CAPS means it is a constant, 
	#don't modify these, they are the templates for the class
	#properties and freatures defines on the class not on the object the class will create 
	#these can be called by using TheNameOfTheClass.Name outside of the class -> ex: Creature.NORMAL
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONC = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"


	def __init__(self):
	#this is where we put the global arguments 

		self.name = ""
		self.state = Creature.NORMAL
		self.health = 20
		self.max_health = 20
		self.attack_points = 2
		self.weapon = None
		self.special_abilities = {}
		self.stats = {}

	def attack(self):
		""" Return the attack value of the creature, given its base attack value, Weapon attack value, and state."""

		#set the attack value to the base attack amount 
		atk_value = self.attack_points

		#If we have a weapon, add the weapon's damage at atk_value 
		if self.weapon:
			atk_value += self.weapon.base_damage

		#return the total calculated damamge 
		return atk_value

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

