"""
Creates a translation program to change english messages into morse code
or to change morse codes messages into english

"""
__author__="Alexis Bird, Gabriel Key, and Sarah Fellows"

# ask if user wants to send or read a message
# if send, receive text for message, translate text to morse code, and write to a file/display
# if read, read morse code file, translate message, and dipslay / write to file


import re
from morse import morse


def main():
    """The main driver function to this Morse Code translator"""
    ######write this last######
    ### create input to receive message that is used in def write_code

    eng_message = input("What is the message you would like to send?")
    file_name2 = input("What would you like to name the file?")
    write_code(eng_message,file_name2)

    #Main should be the only function that prints, all other functions should not
    morse_file = input("What file would you like to translate?")
    print(read_code(morse_file))

def read_code(morse_file):
    """ Accepts morse file name and returns english translation"""
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

                    # concatinate each string

def write_code(eng_message, file_name2):
    """ Accepts english file and returns morse code and file name"""
    # This accepts a message and returns the message in code, prints the code, saves the code to a file,
    # and tells the user the file location.

    # accepts a message ---- done with signature def write_code(message, file_name2):

    # loops through the message, converting each letter in message to morse code
    # use a for loop: "for XXYY in  string:
    #print(eng_message)

    trans_message = ""

    for english_char in eng_message.upper():
        if english_char == " ":
            trans_message += "       "
        elif english_char in morse:
            trans_message += (morse[english_char] + "   ")

    save_code(trans_message, file_name2)

    #     print (m_dict[XXYY] + "   ") ** don't forget to add spaces with "   " after each character
    #    will need an if statement to account for when spaces are met: if ltr = " ",




def save_code(trans_message, file_name2):
    """saving the code to a seperate file"""
    file_name2 = open(file_name2, "w")
    file_name2.write(trans_message)
    file_name2.close()

def open_message(file_name):
    """open a message file for translation to morse code"""
    open_file = open(file_name, "r")

    file_content = open_file.read()

    open_file.close()

    return file_content

# def print_results():
#     # print_results will show each message and its morse code translation.
#     # So, file would contain a message and its code for each action
#     # THis will aslo require a new file that will contain each
#     pass



if __name__ == '__main__':
    main()
