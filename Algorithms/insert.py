def main():

	#Use insertion sort 
	sorted_list = insertion_sort(["E", "Z", "L", "O", "B", "F"])
	print(sorted_list)


#defines the function 
#Swaps two items in a list
#Returns: the list with things swapped. 
def swap(the_list, index_a, index_b):

	the_list[index_a], the_list[index_b] = the_list[index_b], the_list[index_a]

	#Make a temp to hold one value 
	#temp = the_list[index_a]

	#Swap the values
	#the_list[index_a] = the_list[index_b]
	#the_list[index_b] = temp 

	#Return list with swapped items 
	return the_list

def insertion_sort(the_list):
#Sort the list using the insertion algorithim 

	for start_index, value in enumerate(the_list):

		#make a temp variable for the index of the thing we are currently sorting
		lost_index = start_index
		lost_value = value 

		#Look for where the lst index's value belongs 
		while lost_value < the_list[lost_index - 1] and lost_index > 0: 


			#Swap the lost value with its adjacent value 
			the_list = swap(the_list, lost_index, lost_index - 1)

			#decrement the lost_index 
			lost_index -= 1

	#return the sorted list 		
	return the_list

#Call main to sort the things
main()
			






	# 
	# Given a list:

	# 1) Find the length of the list 

	# - determine two lists - sorted and unsorted 

	# - compare the value of the current index in unsorted list with the last index value in sorted list. 

	# - if current index value is smaller than last index in sorted list, insert in front of last index value. 
	# If not, continue checking sorted lists index's values. 

	# -  One end of sorted list is reached, repeat process for next index in unsorted list. 

	# - Repeat until no more items are in unsorted list. 

	# 
