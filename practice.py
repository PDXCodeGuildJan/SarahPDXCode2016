def main():
	print("elephant"[1])
	print("elephant"[5])
	print("elephant"[3:6])

	user_input = input("Please provide a word: ")
	#this allows for the user to input a work 

	middle_characters(user_input)
	#function to be called in the future

	loop(user_input)
	#this will use whatever the user puts in for the loop

	my_list=["cookies", "puppies", "rafting", "soft sheets", "pickles", "rock climbing"]
	#this makes the list
	loop(my_list)
	#this passes the list to the function 


def middle_characters(the_string):
#defining the variable to be called the_string

	#this determines the middle of the variable the_string by finding the length and dividing it by 2
	middle = (len(the_string)//2)

	#this prints out the variable the_string, takes the middle and prints out the middle character as wel as the one before it (-1) and the two after that (+2)
	print(the_string[middle-1:middle+2])
	
#Write a function that expects an input of a sequence, 
#prints out the sequence, loops through the sequence, and prints out each element 
	
def loop(my_list):
#defines the variable loop

	print(my_list)
	#this prints the variable/sequence  
	for x in my_list:
		print(x)
		#this loops through the sequence and prints each element 

main()