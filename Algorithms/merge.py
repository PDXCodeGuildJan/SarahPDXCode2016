__author__ = "Sarah Fellows"

"""Implements the merge sort algorithm, recursively, in Python."""

def main():

	"""Take a random list and use merge_sort to sort it"""

	unsorted = [6, 90, 45, 8, 33, 2, 65, 12]
	sorted = merge_sort(unsorted)
	print(sorted)

def merge_sort(unsorted):

	"""Implement the merge sort algorithm"""

	# Given a list: 

	# split the list into two halfs, if list length is more than 1 
	#If the list length is more than 1... 
	if len(unsorted) > 1:
		#Find the middle of the unsorted listed
		mid = len(unsorted) // 2 
		#Determine what the left_list is by slicing the unsorted list by the 
		#beginning to the middle [:mid]
		left_list = unsorted[:mid]
		#Determine what the right list is by slicing the unsorted list from the middle 
		#to the end [mid:]
		right_list = unsorted[mid:]

		# sort the half using merge_sort - start the recursion processing calling 
		#merg_sort function again 
		left_list = merge_sort(left_list)

		# sort the second half using merg sort  start the recursion processing calling 
		#merg_sort function again 
		right_list = merge_sort(right_list)

		# merge the two sorted lists back together by calling the merge function defined below 
		merged_list = merge(left_list,right_list)

		#return what was found in the line above, calling the merge function left 
		#below using the left and right list 
		return merged_list

	else:
		return unsorted

def merge (left_list, right_list):

	"""Given two lists, merge them together into a third list, which is sorted."""

	temp_list = []
	#this defines an empty list, alertavtive way is: temp_list = list()

	left_i, right_i = 0, 0 
	#A variable that we are calling left_i = 0 and right_i = 0 

	left_len, right_len = len(left_list), len(right_list)
	#this creates the length of the list 

	while left_i < left_len and right_i < right_len:
	#While the left index is less than the legth of the left list 
	#AND while the right index is less than the length of the right list then...

		#if the left list's index value is less than the associated right list's index 
		#value, put it in the temp list and then increase the index by 1 
		if left_list[left_i] < right_list[right_i]:
			temp_list.append(left_list[left_i])
			left_i += 1

		#if the right list's index is less than the associated left list's index value
		#then put it in the temp list and then increase the index by 1 
		else:
			temp_list.append(right_list[right_i])
			right_i += 1

	#take the remaining of the each list using slicing to extend (adding the list to the list)
	#it to the temp list 
	temp_list.extend(left_list[left_i:])
	temp_list.extend(right_list[right_i:])
	
	return temp_list



if __name__ == '__main__':
	main()





