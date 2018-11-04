import random, string


def build_trigrams(fileinput):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    cleaning = str.maketrans('','',string.punctuation)

    #but no error handling yet
    with open(fileinput, 'r') as filehandle:
        #read file, clean newlines and puncuation, make everything lower case for more word matching, put into list
        words = (((filehandle.read().replace('\n', ' ')).translate(cleaning)).lower()).split()
        
        #populate trigrams dictionary
        for i in range(len(words)-2):
            if tuple(words[i:i+2]) in trigrams:
                trigrams[tuple(words[i:i+2])].append(words[i + 2]) 
            else: 
                trigrams[tuple(words[i:i+2])] = [words[i + 2]]

    return trigrams

def build_text(trigrams):
    """
    create a new story from the existing words

    takes the trigrams dictionary and return a list with new text
    """
    #use random to find a starting key in the dictionary
    next_key = random.choice(list(trigrams))

    #add the new key as the first two words to the new list
    new_creation = list(next_key)


    while True:
        #add one of the values from the key to the new list
        new_creation.append(random.choice(trigrams[next_key]))

        #check if new key exists in dictionary and prevent loop if matching old key
        if tuple(new_creation[-2:]) in trigrams and tuple(new_creation[-2:]) != next_key:
            next_key = tuple(new_creation[-2:])
            if len(new_creation) > 200:    #control the length of the new text
                break
        else:
            break
    
    return new_creation




if __name__ == "__main__":

    filename = input("Please enter filename to process> ")

    word_pairs = build_trigrams(filename)
    #print(word_pairs.values())
    #print(word_pairs)
    new_text = build_text(word_pairs)

    print(" ".join(new_text))