import string
import random

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


# todo: select letters by natural frequency
def getRandomLetter(selector):
    if selector == 0:
        return random.choice(consonants)
    else:
        return random.choice(vowels)

# given the rules you must have 4 consonants and 3 vowels we only have 2 letters left to play with
# giving 3 options; 2 vowels, 2 consonants or one of each

# here I use 0 to represent consonants and 1s to represent vowels
def instantiateLetterTypes(x):
    return {
        0:[0,0,0,0,0,0,1,1,1],
        1:[0,0,0,0,0,1,1,1,1],
        2:[0,0,0,0,1,1,1,1,1],
    }.get(x)


def getLettersArray():
    return map(getRandomLetter, instantiateLetterTypes(random.randint(0,2)))
