
#define a function within this module called "selection_sort" that expects a list 
# write a implementation of Selection Sort in this function 

unsorted_list=[6, 17, 9, 34, 4]

print(unsorted_list)
	#Make a list 


def selection_sort(unsorted_list):
#define a function 

	list_length = len(unsorted_list)
	#this finds the length of the unsorted_list

	#Take the first index in the unsorted list 
	first_number = 0
	#this starts the index 

	

	#Repeat this process until list is complete - loop - move up to where you want the loop to start 
	while first_number < list_length:
	#while the index is less than the list length then:
	#this is so that while the index still has numbers to compare to in the length then do the following:
		current_index = first_number
		lowest_index = first_number

		while current_index < len(unsorted_list):
		#while the index is less than the length of the the current index 
			if unsorted_list[lowest_index] > unsorted_list[current_index]:
			#if the value in lowest index of the unsorted list is greater than the value of the current index in the unsorted list:
				lowest_index = current_index

			current_index += 1 

		#swap 
		#current_index, first_number = first_number, current_index

		
		
		temp = unsorted_list[lowest_index]
		unsorted_list[lowest_index] = unsorted_list[first_number]
		unsorted_list[first_number] = temp

			#by calling the unsorted_list[value] it puts in a value instead of the index 

		"""
		Temp = A 
		1st Index = B 
		Lowest Num = c 

		A=B
		B=C 
		C=A

		"""


			#lowest_index[current_index] = unsorted[lowest_index]
		

		#swap smallest number with the first item in the unsorted list. 

		#Update start of unsorted list - Shift the unsorted list to the next index.
		first_number += 1
		#this takes the index first_number and bumps up the index during the next loop around. 
	return unsorted_list


	
sorted_list = selection_sort(unsorted_list)
print(sorted_list)


"""

Bubble Sort 

1) Make a list 

#Find the lenth of the list

2) Compare the first two index's values and determine if the first index's value is greater than the second index's value. 
If it isn't greater, then swap the two values. 

3) Repeat the process for the length of the list.

4) Once the list runs through the end of the length, move the end point in by one. 

5) Repeat process.


Find the first index's value is the first index greater than the value in the second index 


while current_index < len(unsowhile current_index < len(unsorted_list[first_number:])
"""















