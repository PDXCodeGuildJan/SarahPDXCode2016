# Make a text based maze that has 5 rooms, including a start and finish and can handle incorrect inputs 
#gracefully. Handle inputs without case-sensitivity, add some traps, output the path taken at the finish.  


#The first step to any py program is to define the main: 
def main():
	
	#Welcome user to the program 
	print("Welcome to the the Dream Maze! You woke up this morning and thought it was just like every other day. But instead," 
	"you found yourself standing in a desert and you need to find your way home. Help navigate yourself back to to your bed! Type quit to exit at any time!") 
	
	entree = ""
	#clarifying that variable exists 

	while entree !="quit":
	#This is saying that as long as "quit" isn't typed then do the following... 
		
		entree = input("You see magical doors to the left and to the right, which door do you dare take?")
		#Ask the user where they would like to go

		if entree.lower() == "left":
			#if they chose the left door, call the lake function
			lake()
	 
		elif entree.lower() == "right": 
			#if they choose the right door, call the mountain function 
			mountain()

		elif entree.lower() == "quit":
			print("You have chosen to exit the game. Bad choice! Not fun for you! Good Bye!")
			exit()

		else:
			print("I do not understand what you typed. Do you remember your choices?(left/right)")
			
#this is the lake function 
def lake():
	#Tell them what happens when they choose the lake function 
	print("You walked straight into a lake! You must turn around quickly before the lake monster eats you!")
	entree = input("Do you want to turn around? (yes/no)")	
	
	if entree.lower() == "yes":
		main()

	elif entree.lower() == "no":
		#tell them what happens and end the game by not giving it any more functions. 
		print("Oh no! The lake monster has eaten you and you are now dead. Good Day.")

	else:
		print ("I do not understand what you typed. Do you remember your choices?(yes/no)")

def mountain():
	print("You have found yourself standing on a glorious mountain and need to jump before it starts snowing.")
	entree = input("You jump up or jump down. Which way to you choose? (up/down)")

	if entree.lower() == "up":
		ocean()

	elif entree.lower() == "down":
		valley()

	else:
		print("I do not understand what you typed. Do you remember your choices?(up/down)")

def ocean(): 
	print("You are now on the edge of a continent! Quick, turn around before the waves swallow you up!")
	entree = input("Do you want to go back to the mountains?(yes/no)")

	if entree.lower() == "yes":
		mountain()

	elif entree.lower() == "no":
		print("You decided to drown a slow and painful death. Goodbye.")

	else: 
		print("I do not understand what you typed. Do you remember your choices?(yes/no)")

def valley():
	print("Congratulations! You made it out of the mountains and into the valley. Beware, the valley girls will talk your ear off if you dont get out quickly!")
	entree = input("You can go into the forest or into the hills for relief. Which do you chose? (forest/hills)")

	if entree.lower() == "forest":
		forest()

	elif entree.lower() == "hills":
		hills()

	else:
		print("I do not understand what you typed. Do you remember your choices?(forest/hills)")

def forest():
	print("You made it to the lush tree forest that will protect you from the valley girls but not the bears. Hurry and jump into that pile of leaves to take you home!")
	entree = input("Would you like to jump?")

	if entree.lower() == "yes":
		print("Congratulations! You made it back to your bed and you realized that its all a dream!")

	elif entree.lower() == "no":
		print("Oh no! Wrong answer! You must start over!")
		main()

	else:
		print("I do not understand what you typed. Do you remember your choices?(yes/no)")

def hills():
	print("You escaped the girls and found yourself in the high hills overlooking the valley. But the girls are coming to find you. You must start digging a hole in order to escape their chatter.")
	entree = input("Would you like to start digging a hole?(yes/no)")

	if entree.lower() == "yes":
		print("Congratulations! You made it back to your bed and you realized that its all a dream!")

	elif entree.lower() == "no":
		print("Oh no! Wrong answer! You must start over!")
		main()
	else:
		print("I do not understand what you typed. Do you remember your choices?(yes/no)")

main()










