""" This is a way to learn Nodes"""

__author__ = "Sarah Fellows"

def main():
   link = LinkedList()
   link.add(4)
   link.add(2)
   link.add(86)
   link.add(4)
   link.add(7)
   print("Current list:", link)

   link.remove(4)
   print("List after first 4 is removed:", link)

   link.remove(4)
   print("List after second 4 is removed:", link)

   print("Success! Attempt to remove a third 4 yielded no crashes!")
   link.remove(4)


class Node():
	"""Defines the node"""

	def __init__(self,value):
	#this is where we put the global arguments

		self.value = value
		self.next_node = None


class LinkedList():
	""" Defines the Linked List object"""

	def __init__(self):
		#this is where the global arguments are held for the linked list.

		self.head = None #this identifies the start of the head is equal to None 

	def __str__(self):
		""" Creates a function that goes through the list and creates a string of all of the values,then returns the string."""
		#looks at each node, get the value and append it as a string to the list

		#Make a temporary empty string 
		string = ""

		#loop through the list, look at the value of every node and append the value of each node to the temp string 
		
		#Find start of the list, temp variable 
		current_node = self.head

		# loop through the list and add the node to the end of the list 
		while current_node != None: 
			string += str(current_node.value) + ", " #Need to go into the node and stringify the variable 
			
			#Move current node "arrow" down to the next one 
			current_node = current_node.next_node
	
		#return the string to 
		return string

	def search(self,value):
		"""This search function goes through the whole list and returns it""" 
		pass

	def add (self,value):
		"""This add method finds the end node and adds a new one to the end"""
		new_node = Node(value) #create a new Node and giving it the value 

		current_node = head #this makes the list start at the head and makes it the variable current_node 
		
		while current_node.next_node: #While the variable current_node has a value next_node then it will do the following:
			current_node = current_node.next_node #as long as there is a next value 

		current_node.next_node = new_node #when the while loop kicks out to here, its because the 



	def remove (self,value):
		"""This remove methods removes certain nodes"""

		#We need to traverse the list looking for the number we want to remove 

		#need to identify where the head currently is 
		link = self.head

		#identify the second or next node visited to be able to track it 
		#the iternation will stop before it gets to None 
		current_link = None

		#once the number is found, found_link will be true 
		found_link = False 

		#Create a while loop that moved the current link (node) to find the number we are
			#looking for an remove it 
		while current_link not found:
			if link.main() == value:
				#not completed 















