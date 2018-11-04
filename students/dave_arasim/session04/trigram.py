#!/usr/bin/env python
'''Trigram for Session 4, Python 210
Written by David K. Arasim - 10/30/18'''

#Imported modules
import sys
import random
import string
from collections import defaultdict

#Global variables
tri_limit = 2  #Number of words from end of input string to stop creating trigrams

#############################################################################################
#Function section

def main():
    trigram_dict = defaultdict(list)          #Initialize trigram dictionary

#   text_str = 'I wish I may I wish I might'  #Input string from literal string for testing
    text_str = build_text_str()               #Input string from text file supplied by user

    text_out = ''                             #Output string

    text_str_lower = text_str.lower()         #Convert input string to lower case
    text_str_split = text_str_lower.split()   #Split string by default (space char)
    text_str_split_len = len(text_str_split)  #Number of space-delimited words

    #Build the trigram dictionary based on word pairs
    for this_idx in range(text_str_split_len - tri_limit):
        this_key = text_str_split[this_idx] + ' ' + text_str_split[this_idx + 1]
        trigram_dict[this_key].append(text_str_split[this_idx + 2])

    #Printing out trigram dictionary just to see it
    print('trigram_dict: ', trigram_dict)

    #Randomly select a dict key to start the output text string
    random_dict_key = random.choice(list(trigram_dict.keys()))

    #Printing out random dict key just to see it
    print('random_dict_key: ', random_dict_key, '; ', sep = '', end='')

    #Start the output text string with the random dict key
    text_out += random_dict_key

    #Feed the while loop below with the random dict key as 'next_key'
    next_key = random_dict_key
    text_out_end = False

    #Complete the output text string by walking through keys/values
    while not(text_out_end):
        next_values = trigram_dict.get(next_key)
        if next_values:
            print('next_values: ', next_values, '; ', sep = '', end='') #Show all values for this key
            next_val = random.choice(next_values)
            print('next_val: ', next_val)                               #Show randomly-selected value

            text_out += ' ' + next_val

            #Build next key based on last word in last key plus selected value
            next_key = next_key.split()[1] + ' ' + next_val
            print('next_key: ', next_key, '; ', sep = '', end='')       #Show next key
        else:
            #Can't find last key, which will be last two words of input string
            print('key not found')
            text_out_end = True

    print()
    print('text_out: ', text_out)  #Show output string

#############################################################################################

def build_text_str():
    '''Build a text string from text file, all lower-case and stripped of punctuation'''
    text_str = ''
    translator = str.maketrans('', '', string.punctuation)

    print('Enter text file name for text string build: ', end='')
    text_file = input()

    try:
        with open(text_file, 'r') as textfile:
            while True:
                text_line = textfile.readline()
                if not text_line: break

                text_line = text_line.strip()
                text_line = text_line.translate(translator)

                if text_str != '': text_str += ' '
                text_str += text_line

            textfile.close()
    except FileNotFoundError:
        print('File not found')
        sys.exit('Exiting program...')

    return text_str

#############################################################################################
#Main section

if __name__ == "__main__":
    #Guards against code running automatically if this module is imported
    main()