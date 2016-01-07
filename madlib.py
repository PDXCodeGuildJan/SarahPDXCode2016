# Make a madlib that prompts the user for 5 works/phrases and then adds those to a silly story 

madlib = "Today we went on a hunt for "

specific_object = input ("Please tell me an object: ")

madlib = madlib + specific_object + "that can only be found in "

place = input ("Please tell me a your favorite place: ")

madlib = madlib + place + "But to get to this place we had to "

action = input ("Please tell me an action: ")

madlib = madlib + action + "really hard. Then we had to "

action2 = input ("Please tell me another action: ")

madlib = madlib + action2 + "in order to make it there in time to catch the plane. Once we made it on the plane, the flight attendant asked if we would sing "

song = input ("Please tell me your favorite song: ")

madlib = madlib + song + "in order to get the plane moving.  After, we flew to our destination and jumped in a cab. The cab driver asked if we would "

dance = input ("Please tell me your favorite type of dance: ")

madlib = madlib + dance + "in order for him to drive us to our desination. Here, we found what we were looking for."

print(madlib)