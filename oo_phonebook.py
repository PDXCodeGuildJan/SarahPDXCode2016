""" A phonebook program implemented with classes."""

__author__ = "Sarah Fellows"

import re 

def main():

	#test the Contct and Address classes with Jim Everyperson. 
	jim = Contact("Jim", "Everyperson")
	jim.phone_num = "5037209283"
	jim.email = "jim@gmail.com"
	jim.update_address("Home", city="Portland")
	jim.update_address("Work", "4 Fun Lane", "Unit B", "Los Angeles", "CA", "90347", "USA")
	print(jim)

class Contact:
	""" Defines the Contact object to store information about people."""

	def __init__(self, f_name, l_name):
		#Assign past arguements to their corresponding properties 
		#take each property in created chart, add "self.""
		self.first_name = f_name
		self.last_name = l_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street=None, unit=None, city=None, state=None, zip_code=None, country=None):
		""" Update the adress at addy_key with the information passed. """
		
		#check to see if yu already have an address for that key 
		if addy_key in self.addresses:
			temp_address = self.addresses[addy_key]
		else: 
			#Make a new adddress object 
			temp_address = Address()

		#Set the new address' street to whatever was passed. Because None is a built in object, None defalts to false. 
		if street: 
			temp_address.street = street
		if unit:
			temp_address.unit = unit 
		if city: 
			temp_address.city = city 
		if state:
			temp_address.state = state 
		if zip_code:
			temp_address.zip = zip_code 
		if country:
			temp_address.country = country 

		#this is going to store the temp address information in the dictonary at a specific key 
		self.addresses[addy_key] = temp_address

	def format_phone_num(self, phone_num):
		""" Format the phone number of the contact all pretty-like."""
		
		#Scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
		#remove all but the numbers 
		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)

		#Take everything in the list of numbers and make it into a string of nums 
		new_num = ""
		for every_num in nums:
			new_num += every_num

		#Introduce the correct formatting to the string of nums 
		formated_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]

		#Save formated number to Contact 
		self.phone_num = formated_num

	def __str__(self):
		""" Print out the contact's information in a pretty way."""
		
		#Initialize formated string 
		formated_str = "{0} {1}".format(self.first_name, self.last_name)

		#if they have a phone number, then do... 
		if self.phone_num:
			#format the phone number from the formatted function above 
			self.format_phone_num(self.phone_num)
			#Add the pretty phone number to the formated_str
			formated_str += "\nPhone: {0}".format(self.phone_num)

		#if there is an email adddress...
		if self.email:
			formated_str += "\nEmail: {0}".format(self.email)

		#if there is at least one address
		if self.addresses:
			formated_str +="\nAddresses"
			formated_str +="\n--------------------------------------"

			#Loop through all the addresses and print them 
			#Get all the key, value pairs of the addresses using the Dictonary.items function 
			for key, address in self.addresses.items():
				formated_str += "\n{0}:".format(key)
				formated_str += "\n{0}".format(address)
				formated_str +="\n<><><><><><><><><><><><><><><><>"

		return formated_str


class Address:

	"""Defines the Address object to be used with Contact."""

	def __init__(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		""" Print out the address formatted all pretty-like."""

		formated_str = self.street 
		
		if self.unit != "":
			formated_str += "\n" + self.unit

		formated_str += "\n" + self.city + " " + self.state + " " + self.zip_code
		formated_str += "\n" + self.country

		return formated_str 



if __name__ == '__main__':
	main()






