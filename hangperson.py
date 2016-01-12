#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["unicorn", "assignment", "surveyed", "rainbow", "comprehension", "antlers", "armadillo"]
#this makes the list 
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   # (1) Find the length of the word list (words)
   wordchoices = len(words)
   # (2)Create a number to help with the selection 
   num = randint(0,wordchoices-1)
   # (3) use the random number to get the word out 
   chosenword = words[num]

   # Make the randomly selected word into a list object
   listedWord =list(chosenword)

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState

   currentState = []

   for x in listedWord:
      currentState.append("_")

   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   #this is saying while the current state doesn't equal the listedWord and the 
   #wrong guess is under the 6th time then... 
   while currentState != listedWord and numWrong < 6:
      #first, ask the user to guess 
      guess = userGuess()
      #pass
      #this means "dont look at this code" - will need to edit 

      #See if the guess is in the word, update accordingly 
      currentState = updateState(guess, currentState)

      printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly
      if numWrong == 6:
         print("You have guessed incorrectly too many times and you have lost the game! Goodbye!")

      elif currentState == listedWord:
         print("Congratulations you haven chosen all the correct letters! Great job!")



# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)
   #listedWord is the random word that got turned into a list. .count is a built in function 
   #current state is the dashes, underscores - current state of the game 
   #numWrong

   #if the guess doesn't equal 0, then print it is an incorrect choice. 
   if numInWord == 0:
      print("That was an incorrect choice, please try again!")

      #this then adds it to memory 
      numWrong = numWrong + 1
         #shorthand for this is numWrong += 1

   # If it isn't, tell the user and update the numWrong var
   # If it is, congratulate them and update the state of the game.
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   elif numInWord > 0:
      print("Great guess! There is " + str(numInWord) + " of the letter " + guess + " in the word")
      #another way to do it is: print("Yes, there is {0} of the letter {1} in the word".format(numInWord, guess))
      #check to see if each letter is a match and if it is, fill it in the spot
      
      #While we still have letters to find, keep looping -> we know it will be a while loop
      numFound = 0 
      index = 0
      #this starts the search at the 0 slot in the list 
      while numFound < numInWord and index < len(listedWord):
         #See if letter is in word at index 
         if listedWord[index] == guess:
         #if the word that was randomly selected by the game made into a list, if at the first index 
         # the letter is the same as stored inside guess, then we will do something 
            
            currentState[index]= guess
            #this takes whatever is in the current state, uses the index to input the guess 

            numFound += 1
            #Then this says I found one and then adds it to the memory of numFound

         index += 1 
         #incrementing the index 




   return currentState


# This helpful function prompts the user for a guess,
# accepting only single letters.

#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   
   while len(guess) != 1:

      #user has given us too long of a response check if it is an exit, then exit if it is 
      if guess.lower() == "exit":
         print("You have chosen to exit the game. Bad choice. Goodbye!")
         exit()

      #otherwise, ask them to guess again 
      else: 
         guess = input("You have typed more than one letter. Please guess again!")


   return guess


#### DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()
