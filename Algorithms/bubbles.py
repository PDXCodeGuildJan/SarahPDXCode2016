unsorted_list=[6, 17, 9, 34, 4]

print(unsorted_list)

def bubble_sort(unsorted_list):
#define a function

    listLength = len(unsorted_list)
    # 1)Find the length of the list

    #2) Compare the value of the current index and compare it with the value of the next index.
    firstItem = 0

    while firstItem < listLength -1:
    #this starts the outter loop
        currentIndex = firstItem

        while currentIndex < listLength - 1:
        # need to establish an inner while loop - this says that while the current Index has any length
        #to use for comparison, keep loop but decrease the length by one each time

            # 3) Determine if value of current index is is greater than value of next index.
            if unsorted_list[currentIndex] > unsorted_list[currentIndex+1]:

                # 4) If it greater, swap with next index. If it is not greater, do nothing.
                #unsorted_list[currentIndex], unsorted_list[currentIndex+1] = unsorted_list[currentIndex+1], unsorted_list[currentIndex]
                tempSpot = unsorted_list[currentIndex]
                unsorted_list[currentIndex] = unsorted_list[currentIndex+1]
                unsorted_list[currentIndex+1] = tempSpot

            currentIndex += 1
            #this makes sure that the index does up by one index each loop

        listLength -= 1
        #6) Once end is reached, move the end point in by one.

    return unsorted_list

sorted_list = bubble_sort(unsorted_list)
print(sorted_list)

"""

Bubble Sort
Given a list:

1) Find the lenth of the list

    2) Compare the value of the current index and compare it with the value of the next index.
    3) Determine if value of current index is is greater than value of next index.
    4) If it greater, swap with next index. If it is not greater, do nothing.

    5) Change current index to next index, repeat process for the length of the list.

6) Once end is reached, move the end point in by one.

7) Repeat process.

while current_index < len(unsorted_list[first_number:]):
#this moves
"""


    #2) Compare the value of the current index and compare it with the value of the next index.

    #for firstItem,value in enumerate(unsorted_list):
    #this starts the outter loop

        #currentIndex = firstItem

        #if currentIndex


    #Does the currentIndex need to be identified as the lowest index?
