def main():

    unsorted_list = [6, 17, 9, 34, 4]

    print("original", unsorted_list)
    #Make a list 

    sorted_list = selection_sort(unsorted_list)
    print("selection", sorted_list)

    sorted_list = bubble_sort(unsorted_list)
    print("bubble", sorted_list)

#define a function within this module called "selection_sort" that expects a list 
# write a implementation of Selection Sort in this function 
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
        #swap smallest number with the first item in the unsorted list. 

        #Update start of unsorted list - Shift the unsorted list to the next index.
        first_number += 1
        #this takes the index first_number and bumps up the index during the next loop around. 
    return unsorted_list


"""
---------------- Bubble Sort  ----------------------
"""

def bubble_sort(unsorted_list):
#defines the function 

    # 1) Find the length of the list 
    list_length = len(unsorted_list)

    # 2) Compare the value of the current index and compare it with the value of the next index.
    
    first_item = 0 
    #this says that the first index spot is now called first_item 

    while first_item < list_length -1:
    #this starts the outter loop - as long as the index is less than the length of the list 
    #(subtract one to avoid infanite loop)

        current_index = first_item
        #this assigned current_index to be the first index - 0 


        while current_index < list_length -1:
        #starts the inner loop
        # this says that while the current Index has any length
        #to use for comparison, keep loop but decrease the length by one each time

            # 3) Determine if value of current index is is greater than value of next index. 
            if unsorted_list[current_index] > unsorted_list[current_index+1]:

                tempSpot = unsorted_list[current_index]
                unsorted_list[current_index] = unsorted_list[current_index+1]
                unsorted_list[current_index+1] = tempSpot

            current_index += 1

        list_length -= 1

    return unsorted_list


main ()





























