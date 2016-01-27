""" A phonebook program implement with classes."""

__author__ = "Sarah Fellows"

class Contact:
	""" Defines the Contact object to store information about people."""

	def __init__(self, f_name, l_name):
		#Assign past arguements to their corresponding properties 
		self.first_name = f_name
		self.last_name = last_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street="", unit="", city="", state="", zip="", country=""):
		""" Update the adress at addy_key with the information passed. """
		pass 

	def format_phone_num(self, phone_num):
		""" Format the phone number of the contact all pretty-like."""
		pass

	def print_contact():
		""" Print out the contact's information in a pretty way."""
		pass 

class Address:

	"""Defines the Address object to be used with Contact."""

	def __init___(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str___(self):
		""" Print out the address formatted all pretty-like."""

		formated_str = self.street 
		
		if self.unit != "":
			formated_str += "\n" + self.unit

		formated_str += "\n" + self.city + " " + self.state + " " + self.zip_code
		formated_str += "\n" + self.country

		return formated_str 










