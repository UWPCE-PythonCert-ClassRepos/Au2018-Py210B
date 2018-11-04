import random

words = "I wish I may I wish I might".split()
# words

def trigrams(x,n,m):
trigram_dic = {}
for i in range(len(words)-2): #looking to see how many words do we have in the sentence print(i)
    pair = tuple(words[i:i + 2]) #creating my keys looking at each word + 2 print(pair)
    follower = words[i + 2] #looking for each world after the combination
    trigram_dic.setdefault(pair,[]).append(follower) # creating list a
    #trigrams = list(random.choice(list(a.keys())))
    words_count = m #how long the sentence going to be 
    result = [] 
    start_tuple = random.choice(list(trigram_dic.keys()))
    result.append(start_tuple[0])
    result.append(start_tuple[1])
    while len(result) < words_count:
        if start_tuple not in trigram_dic:
            result[-1] = result[-1]+"."
            start_tuple = random.choice(list(trigram_dic.keys()))
            result.append(start_tuple[0])
            result.append(start_tuple[1])
        nextWord = random.choice(trigram_dic.get(start_tuple))
        result.append(nextWord)
        start_tuple = (start_tuple[1], nextWord)
    return " ".join(result)
trigrams(words,3,33)