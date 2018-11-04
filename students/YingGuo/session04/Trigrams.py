#!/usr/bin/env python3

"""Session 04, assignment:Trigrams, student name: Ying Guo"""

words = "I wish I may I wish I might good morning good afternoon hahahahaha lala hahaha".split()

from collections import defaultdict
import random

def build_trigrams(words):

    trigrams = defaultdict(list)

    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        trigrams[pair] += [follower]
    
    print("This is the Trigrams:")
    for k, v in trigrams.items():
        print(k, ":", v)

    return trigrams
        
def build_text(trigram_dict):
    key_lst = list(trigram_dict.keys())
    print("This is the Tuple key list:\n", key_lst)
    fst_item = random.choice(key_lst)
    new_lst = [fst_item[0].capitalize(),fst_item[1]]
    while len(new_lst) <=200:
        key_tuple = (new_lst[-2],new_lst[-1])
        if key_tuple in key_lst:
            add = random.choice(trigram_dict[key_tuple])
            new_lst += [add]
        if key_tuple not in key_lst:
            break
    new_text = " ".join(new_lst + ["!"])
    print("This is new text: \n", new_text)
    return new_text

def in_data(file_name):
    words_lst = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            a = line.strip().split()
            words_lst += a
    return words_lst


if __name__ == "__main__":
    try:
        user_input = input("What's the file name?")
    except:
        print("pass in a file name")
    
    words = in_data(user_input)
    trigram_dict = build_trigrams(words)
    new_text = build_text(trigram_dict)
