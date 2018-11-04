#!/usr/bin/env python3 
import random
# path C:\\Users\\AMinavi1\\Au2018-Py210B\\students\\aminavi\\session04\\
# file name pg20151.txt

def read_file():
    fp = input("please enter the path ")
    fn = input("please enter the file name ")
    # fp = 'C:\\Users\\AMinavi1\\Au2018-Py210B\\students\\aminavi\\session04\\'
    # fn = 'pg20151.txt'
    f = open(str(fp + fn)) # Open file
    words = f.read() # Read file
    f.close() # Close file
    words = words.split()
    block_of_lines = []
    input_data = open(str(fp + fn))
    for line in input_data:
        if line.strip() == '***START OF THE PROJECT GUTENBERG EBOOK HIDDEN TREASURES***':
            break
    for line in input_data:
        if line.strip() == '***END OF THE PROJECT GUTENBERG EBOOK HIDDEN TREASURES***':
            break
        block_of_lines.append(line)
    return block_of_lines

def trigrams(words,n,m):
    trigram_dic = {}
    for i in range(len(words)-n): #looking to see how many words do we have in the sentence print(i)
        pair = tuple(words[i:i + n]) #creating my keys looking at each word + 2 print(pair)
        follower = words[i + n] #looking for each world after the combination
        trigram_dic.setdefault(pair,[]).append(follower) # creating list a
    #trigrams = list(random.choice(list(a.keys())))
    words_count = m #how long the sentence going to be 
    result = [] 
    start_tuple = random.choice(list(trigram_dic.keys()))
    result.append(start_tuple[0])
    result.append(start_tuple[1])
    while len(result) < words_count:
        if start_tuple not in trigram_dic:
            # result[-1] = result[-1]+"."
            start_tuple = random.choice(list(trigram_dic.keys()))
            result.append(start_tuple[0])
            result.append(start_tuple[1])
        nextWord = random.choice(trigram_dic.get(start_tuple))
        result.append(nextWord)
        start_tuple = (start_tuple[1], nextWord)
    print(" ".join(result))

Trigram_Biogram = input("please enter a number for Trigram Biogram ")
lenght_of_sentence = input("please enter a number for lenght of sentence ")

if __name__ == '__main__':
    trigrams(read_file(),int(Trigram_Biogram),int(lenght_of_sentence))
