#Search functions, including Binary

from sort import bubble_sort
#This imports another file from the same folder, then calls the function 

def main():
	#Make a list to look through, and the target value 
	unsorted_list = ["E", "Z", "L", "O", "B", "F"]
	target_value = "B"

	#going to return the sorted list and the target index
	sorted_list, target_index = binary_search(unsorted_list, target_value)

	#Print out our solutions 
	print("I found", target_value, "It's at", target_index)


def binary_search(the_list, target_value):
	#Implements the Binary Search algorithm 


	#First, sort the list
	sorted_list = bubble_sort(the_list)

	#Search for the target value 

	#Find length of current segment. 
	length = len(sorted_list)

	#initialize start and end variables 
	start = 0 #this determines the start of the list 
	end = length #this determines the end of the list 

	#If length is >= 1, look for target
	while length >= 1:

		#find the current length and middle of the segment of the list we're looking in 
		# Double slashes will give you a whole number, a single slash will give you a float(i.e. a decimal - ex: 2.0)
	
		mid = start + (length // 2)

		#once found, determine if middle value is greater or less than, or equal to and length 
		#If equal, we've found it, return middle (this looks for the best case first)
		if sorted_list[mid] == target_value:
			return(sorted_list, mid)

		#If greater than, reduce segment to left half from middle 
		elif sorted_list[mid] > target_value:
			length = len(sorted_list[start:mid])
			end = mid

		#If less than, reduce segment to right half from middle 
		elif sorted_list[mid] < target_value:
			start = mid + 1	

		#reevaluate length before the loop runs	
		length = len(sorted_list[start:end])

	#defalt response, oh crap - if we can't find the index, return -1
	return(sorted_list, -1)

# Call main to sort the things
if __name__ == "__main__":
	main()