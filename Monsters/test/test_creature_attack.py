__author__ = "Sarah Fellows"

import unittest 

#import the class where the functions lives that you're testing 
#from file creature we are importing the class Creature 
from creature import Creature, Weapon

#Make a new TestCase, CreatureAttackTest, which inherits from unittest.TestCase
#inhertitance - the one of the left can pull from anything on the right 
#the file is named what you are testing and so is the class 
class CreatureAttackTest(unittest.TestCase): 

    #Make the things and do the setup that every test in the TestCase
    #two functions recommended that you do: set up and tear down 
    #when python runs the test file, it will run each test in the test file, 
        #it will run the set up before every test and tear down after every test
    def setUp(self): 
        """Create an instance of the Creature class that we can leverage its 
            functions in our tests. """

        self.creature = Creature()

    def tearDown(self):
        """ Delete the Creature instance we made in the setUp.""" 

        del self.creature

    #attack():int (<-damage)
    #do we get an intager back? 
    #without weapon, does it do base damamge?
    #with weapon, does it do expected damage? 
    #when WEAKENED, does it do half damage?
    #when WEAKENED with weapon, does it do half damage 

    def test_attack_return_int(self):
        """Ensure that when attack is called, an int is returned."""

        # Call the attack function of our creature, and catch what it returns in value
        value = self.creature.attack()

        #assertIS -> testing that the first & second is the same type of object
        #tried self.assertIs(value, 2, "Return Atk value is not an int"), did not work. 
        self.assertIsInstance(value, int, "Return Atk value is not an int")

    def test_no_weapon_return_base_damage(self):
        """Ensure that with no weapon equiped, the creature does it base damage"""

        #manually set the base damage to 2
        self.creature.attack_points = 2

        #get the creature's attack value
        value = self.creature.attack()

        self.assertEqual(value, 2, "Expected base attack value not given.")

    def test_with_weapon_return_damage(self):
        """Ensure that with weapon, the creature does base damage + Weapon damage."""

        #Make a weapon to give to creature 
        weapon = Weapon(3)

        #Give the weapon to the creature 
        self.creature.weapon = weapon 

        #set creature's base attack value 
        self.creature.attack_points = 3

        #Get the creature's total attack value 
        value = self.creature.attack()

        #Assert the attack value is the base + weapon damage 
        self.assertEqual(value, 3 + 3)













