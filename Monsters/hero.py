from creature import Creature 
from monster import Monster

class Hero(Creature):


	def __init__(self):
		super(Hero, self).__init__()

		self.level = 1


class MonsterHero(Monster,Hero): 
	""" This class Monster_hero implements the monster with the hero in the case of multi inhertitance. """

	SECOND_WEAPON = None

	def __init__(self):
		Monster.__init__(self) 
		Hero.__init__(self)

		#self.weapon = Monster_hero.SECOND_WEAPON