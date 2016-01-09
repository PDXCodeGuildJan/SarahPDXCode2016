# Make a text based maze that has 5 rooms, including a start and finish and can handle incorrect inputs 
#gracefully. Handle inputs without case-sensitivity, add some traps, output the path taken at the finish.  


#The first step to any py program is to define the main: 
def main():
	
	#Welcome user to the program 
	print("Welcome to the the Dream Maze! You woke up this morning and thought it was just like every other day. But instead," 
	"you found yourself standing in a desert and you need to find your way home. Help navigate yourself back to to your bed!") 
	#Ask the user where they would like to go
	entree = input("You see magical doors to the left and to the right, which door do you dare take?")

	
	if entree == "left":
		#if they chose the left door, call the lake function
		lake()
 
	if entree == "right": 
		#if they choose the right door, call the mountain function 
		mountain()
		
#this is the lake function 
def lake():
	#Tell them what happens when they choose the lake function 
	print("You walked straight into a lake! You must turn around quickly before the lake monster eats you!")
	entree = input("Do you want to turn around? (yes/no)")	
	
	if entree == "yes":
		main()
	elif entree == "no":
		#tell them what happens and end the game by not giving it any more functions. 
		print("Oh no! The lake monster has eaten you and you are now dead. Good Day.")

def mountain():
	print("You have found yourself standing on a glorious mountain and need to jump before it starts snowing.")
	entree = input("You jump up or jump down. Which way to you choose?")

	if entree == "up":
		ocean()

	elif entree == "down":
		valley()

def ocean(): 
	print("You are now on the edge of a continent! Quick, turn around before the waves swallow you up!")
	entree = input("Do you want to go back to the mountains?(yes/no)")

	if entree == "yes":
		mountain()

	elif entree == "no":
		print("You decided to drown a slow and painful death. Goodbye.")

def valley():
	print("Congratulations! You made it out of the mountains and into the valley. Beware, the valley girls will talk your ear off if you dont get out quickly!")
	entree = input("You can go into the forest or into the hills for relief. Which do you chose? (forest/hills)")

	if entree == "forest":
		forest()

	elif entree == "hills":
		hills()

def forest():
	print("You made it to the lush tree forest that will protect you from the valley girls but not the bears. Hurry and jump into that pile of leaves to take you home!")
	entree = input("Would you like to jump?")

	if entree == "yes":
		print("Congrations! You made it back to your bed and you realized that its all a dream!")

	elif entree == "no":
		main()

def hills():
	print("You escaped the girls and found yourself in the high hills overlooking the valley. But the girls are coming to find you. You must start digging a hole in order to escape their chatter.")
	entree = input("Would you like to start digging a hole?(yes/no)")

	if entree == "yes":
		print("Congrations! You made it back to your bed and you realized that its all a dream!")

	elif entree == "no":
		main()

main()










