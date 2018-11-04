#!/usr/bin/env python3 
import random

def trigrams(x,n,m):
    trigram_dic = {}
    for i in range(len(x)-n): #looking to see how many words do we have in the sentence print(i)
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
    return " ".join(result)



def read_file():
    fp = ".\\students\\aminavi\\session04\\"
    fn = 'pg20151.txt'
    f = open(str(fp+ fn)) # Open file
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


if __name__ == '__main__':
    trigram = trigrams(read_file,n,m)
        print(trigram)