
import collections
import os
import random
import sys

# Return a string of words read from file
def read_in_data(filename):
    in_data = ''
    with open(filename, "r") as file:
        in_data = file.read()
    
    return in_data

# Return a list of words
def make_words(in_data):
    return in_data.split()

# Return a dict that contains words and their followers list
def build_trigram(words):
    words_dict = collections.defaultdict(set)

    for i in range(len(words)-2):
        words_dict[f"{words[i]} {words[i+1]}"].add(words[i+2])

    return words_dict

def build_text(words_dict):

    # Choose starting words randomly
    txt = random.choice(list(words_dict.keys()))

    # Maintain a list of current words list
    l = txt.split()

    # The new text won't be longer than the length of dict
    i = len(words_dict)

    while(i > 0):
        next_values = list(words_dict[" ".join(l[-2:])])

        # if followers exist, pick a random one
        if next_values:
            cur = random.choice(next_values)
            l.append(cur)
            txt = txt + " " + cur
            i -= 1
        else:
            break

    return txt

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)