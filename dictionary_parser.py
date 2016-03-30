import letter_generation
import itertools

dictionary = dict()

file = open('words/354984si.ngl', 'r')
for line in file:
    line = line.strip()
    if len(line) > 3 and len(line) < 10 and line.isalpha() and line[0].islower():
        myKey = ''.join(sorted(line))
        if dictionary.has_key(myKey):
            dictionary[myKey].add(line)
        else:
            dictionary[myKey] = set([line])
file.close()

def checkword(inputword):
    if dictionary.has_key(''.join(sorted(inputword))):
        return dictionary[''.join(sorted(inputword))]
    else:
        return False

def find_largest_anagram(inputword):
    ##print "Input Letters: " + inputword
    for index in reversed(range(3,len(inputword)+1)):
        combos = itertools.combinations(inputword, index)
        for combo in combos:
            result = checkword(''.join(combo))
            if result != False:
                return result

    return "No Anagrams Found"

print "Highest Anagram: " + str(find_largest_anagram(letter_generation.getLettersArray()))

s = """\
from __main__ import find_largest_anagram
from __main__ import letter_generation
"""
if __name__ == '__main__':
    import timeit
    print (timeit.timeit("find_largest_anagram(letter_generation.getLettersArray())", setup=s, number=10000 ))
