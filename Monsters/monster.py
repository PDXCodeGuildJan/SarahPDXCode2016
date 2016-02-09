from creature import Creature 
#from file creature, import the class Creature

class Monster(Creature):
#by doing that, our Monster class will have all the property and methods (object inheritance) 

	AGGRO = "aggressive"
	DEFENSE = "defensive"


	def __init__(self):
		#super a built in variable that represents the class it is inherted from 
		#it will take the __init__ information from creature.py and place it here 
		super(Monster, self).__init__()

		self.personality = Monster.AGGRO
		

