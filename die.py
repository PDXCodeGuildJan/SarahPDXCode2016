from random import randint

#Create a die function that returns a random number, as if the user rolled a die.
def die():
	roll = randint(1,6)
	print (roll)



#Make a function called custom_die that takes a range and returns a random number in that range 
def custom_die(low,high):
	roll = randint(low,high)

	#Determine if max or min 
	if roll == low:
	#if the roll is low, then print below 
		print ("{r} Critical Fail!".format(roll))
		#this is how to use the .format
	elif roll == high:
	#else if the roll is high, then print below 
		print (roll, " Critical Hit!")
		#this is the original way to use the comma for string instead of str()
	else: 
	#else if it doesn't match the top two then print the rest of the roll 
		print (roll)

def main():
	#Prompt for user to exit before the game starts
	print("Welcome to Die Roller. Enter q to exit.")

	entree = ""
	#this is for the while loop

	#Wrap the core logic of the function in a while loop, so that it keeps asking to roll, until we exist.
	while entree !="q": 

		#Ask the user how many dice to roll
		entree = input("How many dice do you want to roll")
		if entree == "q":
			#Exit the program
			exit()

		#int turns the () into a number instead of a character 	
		total_rolls = int(entree)

		#Find out how big the Dice are
		entree = input("How many sides on the dice?")
		if entree == "q":
			#Exit the program 
			exit()
		max_num = int(entree)

		#Roll that many dice 
		for something in range(0, total_rolls):
			custom_die(1, max_num)

main()