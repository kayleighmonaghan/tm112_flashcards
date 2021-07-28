# flashcards_1.py
"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary entries. It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program
"""

from random import *
import csv

def show_flashcard():
    # show flashcard
    random_entry = choice(list(glossary))
    print('Define: ', random_entry)
    input('Press return to see definition')
    print(glossary[random_entry])

def file_to_dictionary(filename):
    """
    Return a dictionary with the contents of a file
    """
    file = open(filename, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary

# set up the glossary
glossary = file_to_dictionary('TM112_Glossary.txt')

message = 'Type "s" for a new flashcard, or "q" to quit:  '
quit = False                  
while not quit:
    user_input = input(message)
    if user_input == 's':
        show_flashcard()
    elif user_input == 'q':
        quit = True
    else:
        print('You must type "s" or "q"')


