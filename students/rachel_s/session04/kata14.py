#!/usr/bin/env python3

import string

with open("sherlock_small.txt") as f:
    words = f.read().strip().replace("\n", " ").split()

f.close


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if not pair in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair] += [follower]

    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
