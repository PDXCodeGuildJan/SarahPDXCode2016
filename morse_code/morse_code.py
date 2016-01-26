"""
Creates a translation program to change english into morse code
or to change morse code into english.

"""
__author__="Alexis Bird, Gabriel Key, and Sarah Fellows"

import re
from morse import morse

def main():
    """The main driver function to this Morse Code translator"""

    # create input to receive message that is used in def write_code
    eng_message = input("What is the message you would like to send? ")
    #create input to ask what file they would like translated
    created_file = input("What would you like to name the file? ")
    write_code(eng_message,created_file)

    #Main should be the only function that prints, all other functions should not
    morse_file = input("What file would you like to translate? ")
    print(read_code(morse_file))

def read_code(morse_file):
    """ Accepts content in a string from specified morse file and returns English translation in a string"""
    # This creates a function that accepts a filename and
    # returns the English translation of the contents of the file.
    untranslated_code = open_message(morse_file)
    translated_code = ""
    # Split at 7 space block for list of words
    word_list = re.split("       ", untranslated_code) # 10 spaces rather
        # than 7 spaces to account for the three spaces between symbols
        # for each word in list of words
    for word in word_list:
        # split each word at 3 space block to create list of symbols
        symbol_list = re.split("   ", word)
            # convert each symbol into equivalent letter
        for symbol in symbol_list:
            for letter, char in morse.items():
                if symbol == char:
                    translated_code += letter

        translated_code += " "

    return translated_code

def write_code(eng_message, created_file):
    """ Accepts english file in a string and returns morse code and file name"""
    # This accepts a message and returns the message in code, prints the code, saves the code to a file,
    # and tells the user the file location.

    # creating an empty string to put the traslated messsage in
    trans_message = ""

    #Loops through every character in the message
    for english_char in eng_message.upper():
        #Take every space in english message and replace with seven spaces in the morse code translation
        if english_char == " ":
            trans_message += "       "
        #Using the dictonary to make a new string using the morse values associated with each english character
        elif english_char in morse:
            trans_message += (morse[english_char] + "   ")

    save_code(trans_message, created_file)

    #     print (m_dict[XXYY] + "   ") ** don't forget to add spaces with "   " after each character
    #    will need an if statement to account for when spaces are met: if ltr = " ",

def save_code(trans_message, created_file):
    """saving the code to a seperate file"""
    created_file = open(created_file, "w")
    created_file.write(trans_message)
    created_file.close()

def open_message(file_name):
    """open a message file for translation to morse code"""
    open_file = open(file_name, "r")

    file_content = open_file.read()

    open_file.close()

    return file_content

if __name__ == '__main__':
    main()
