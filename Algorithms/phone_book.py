""" Phone Book Fun - write a module with functions that adds to, removes from, searches through
and prints a Dictonary that stores names an dphone numbers. 
(names are the keys, phone numbers the values, etc.)"""
	
"""Implements a very simple Phonebook using a Dictonary."""

__author__ = "Sarah Fellows"

import re 

#Initalize our dictonary, which will store our phone numbers 
phonebook = {}

#1 give it information 
def main():
	"""The main drivers function of our Phonebook."""

	#load any existing data into phonebook by calling load_phonebook function 
	load_phonebook()
	#print("Phonebook after load", phonebook) - debugging print statement 
	
	print("\n\tWelcome to our super Fancy Phonebook!")

	option = ""

	while option != "E":

		#Ask the user what they would like to do:
		option = input("\n\tYou can (A)dd, (D)elete, (S)earch or (P)rint your contacts.\n\tTo Search by phonenumber, select (N).\n\tWhat would you like to do?. \n")

		if option.upper() == "A": 
			name = input ("\nWhat is the name of your new contact?")
			number = input("What is " + name + "'s number?")
			add_contact(name, number)

		elif option.upper() == "D":
			name = input ("What contact would you like to delete?")
			delete_contact(name)
		elif option.upper() == "E":
			print("You have chosen to exit the phonebook. Good Day!")
			exit()
		elif option.upper() == "P":
			print_phonebook()
		elif option.upper() == "S":
			name = input("What contact would you like to find? Please tell me their name:")
			search(name)
		elif option.upper() == "N":
			search_number = input("What is the number you wish to search for?")
			search_by_number(search_number)
		else:
			print("I'm sorry, I did not understand. Please choose 'A', 'D' or 'E'. ")

		# add_contact("Sarah", "(503) 720-8294")
		# add_contact("Mom", "(503) 799-8945")
		# add_contact("Christopher", "(503) 720 -9470")
		# print (phonebook) 


def add_contact(name, phonenumber):
	"""Does an addition to the Phonebook with the given contact info."""

	#remove any lingering while space that might have been added 
	#first we need to catch it because it will return it to me 
	#re means we are going to use the import re we put in above and the . means that we are going to us a built in function 
	regex = "\s+\Z"
	#\s means any space and the + means any number of spaces, \Z any amount of spaces at the end of the string 
	thing_you_replace_with = ""
	#regex = "[a-zA-Z0-9_]" - this is another way to do the above regex = \w+
	scrubbed_name = re.sub(regex, thing_you_replace_with, name)
	print(scrubbed_name)

	new_reg = "\w+"
	new_name = re.search(new_reg, name)

	#Scrub and reformat the phone nmber to follow (xxx) xxx-xxxx pattern 
	#remove all but the numbers
	regex = "[0-9]+"
	nums = re.findall(regex,phonenumber)
	new_num = ""
	for every_num in nums:
		new_num += every_num

	#Introduce the correct formatting 
	formated_num = "(" + new_num[0:3] + ")" + new_num[3:6] + "-" + new_num[6:]

	#at the key "name" inside phonebook, add phonenumber 
	phonebook [scrubbed_name] = formated_num
	print("\nNew Contact:", scrubbed_name, "was added with number", formated_num)
	
	#Save updated phonebook 
	save_phonebook()

def delete_contact(name):
	""" removes the given contact from the Phonebook"""
	if name in phonebook:
		del phonebook[name]
		print(name, "was deleted from the Phonebook.\n")

		#save updated phonebook 
		save_phonebook

	else:
		print("That contact does not exist.\n")

def search(name):
	"""Find and print the info of a contact given their name"""
	#if "key" is not in "dictonary" (this is a python built in function):
	if name in phonebook:
		number = phonebook[name]
		print(name, "'s number is:", number)
	else:
		print("Sorry, no contact exists with that name.\n")

def search_by_number(search_number):
	"""Find who a certain number is associated with."""
	#name_of_the_dictonary.items - returns the items in dictory 
	#Giving us back key, value pairs 
	# for key.value in dictonary.items()
	results = ""
	for name, number in phonebook.items():
		if search_number == number:
			print(name, "'s numbr is:", number)
			result = name

	if result == "":
		print("Sorry, no contact has that number.")


def print_phonebook():
	"""Print every contact in the Phonebook."""

	print("----------Contacts:----------")
	for item in phonebook:
		print(item, "has phone number", phonebook[item])

def save_phonebook():
	"""Save the contents of this phonebook to a file"""

	#load data from a file into phonebook
	open_file = open("phonebook.txt", "w")
	#we need to open the file and input data into it, but the write function needs to be converted to a string 
	open_file.write(str(phonebook))
	open_file.close()

def load_phonebook():
	"""Load the phonebook data from the save file"""

	#this gives the new phone book access to the global phonebook to change the memory access point 
	global phonebook

	#Open the file in write mode first, to create it if it doesnt already exist 
	load_file = open("phonebook.txt", "a")
	load_file.close()

	#make a variable to open the phonebook file in read mode 
	load_file = open("phonebook.txt", "r")
	#this will take all of the data in that file and put it into phonebook_data 
	phonebook_data = load_file.read()
	load_file.close()

	#print("String from the file", phonebook_data) - debugging print statement 

	#if there is phonebook data , then load it into the dictonary 
	if phonebook_data:
		#Convert from string back to dictonary 
		#cast it to a dictonary - eval takes a string and turns it into a data function that makes the most sense. Since 
		#looks like a dictonary, it will turn it into a dictonary 
		phonebook = eval(phonebook_data)

	#print("Data in dictonary:", phonebook) - debugging print statement 


if __name__ == '__main__':
	main()











