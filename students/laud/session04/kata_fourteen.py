#!/usr/bin/env python3
import sys
import random
import string
# Strip out punctuations, etc
def cleanup(text):
    # out = "".join( c for c in string if c not in ('!', ',', '.', ':', '(', ')') )
    lowercase = text.lower()
    exclude = set(string.punctuation)
    out = ''.join( ch for ch in lowercase if ch not in exclude)
    return out

# Read txt file
def read_in_data(filename):
    with open(filename, 'r') as text:
        data = text.read()
        clean = cleanup(data)
    return clean

# Split text into list
def make_words(in_data):
    data = in_data.split()
    return data

# Build key-value pairs
def build_trigram(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair not in trigrams:
           trigrams[pair] = []
        trigrams[pair].append(follower)
    return trigrams

# Generate new text
def build_text(word_pairs):
    word_list = []
    starting_pair = list(random.choice(list(word_pairs)))
    word_list.extend(starting_pair)
    for x in range(len(word_list)):
        current_key = tuple(word_list[-2:])
        if current_key in word_pairs:
            next_word = random.choice(list(word_pairs[current_key]))
            word_list.append(next_word)
        else:
            continue
    new_text = " ".join(word_list)
    return new_text
        
if __name__ == "__main__":
    # Get file name from command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)