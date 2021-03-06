import letter_generation
import itertools

dictionary = dict()

##
##  Leaving this stuff in to show how the masterlist.txt was compiled
##  added bonus of not having to do all the checking when parsing that file
##

#filter = set()
#words = set()

#filter_file = open('words/wordslist.txt', 'r')
#for line in filter_file:
#    if line[0].isupper():
#        line = line.strip().lower()
#        filter.add(line)
#filter_file.close()

#file = open('words/354984si.ngl', 'r')
#for line in file:
#    line = line.strip()
#    if len(line) > 3 and len(line) < 10 and line.isalpha() and line not in filter:
#        myKey = ''.join(sorted(line))
#        words.add(line)
#        if dictionary.has_key(myKey):
#            dictionary[myKey].add(line)
#        else:
#            dictionary[myKey] = set([line])
#file.close()

#outfile = open('words/masterlist.txt', 'w')
#for elem in words:
#    outfile.write(elem + '\n')

#file = open('words/masterlist.txt', 'r')
#for line in file:
#    line = line.strip()
#    myKey = ''.join(sorted(line))
#    if dictionary.has_key(myKey):
#        dictionary[myKey].add(line)
#    else:
#        dictionary[myKey] = set([line])

file = open('words/masterlist.txt', 'r')
for line in file:
    line = line.strip()
    myKey = ''.join(sorted(line))
    if dictionary.has_key(myKey):
        dictionary[myKey].add(line)
    else:
        dictionary[myKey] = set([line])
file.close()

##  I tested this with the dictionary.get(key, default = None) function but
##  it worked out to be considerably slower than this version, I assume the comparison
##  to None on the other receiving function was slowing it down
def checkword(inputword):
    if dictionary.has_key(''.join(sorted(inputword))):
        return dictionary[''.join(sorted(inputword))]
    else:
        return False

def find_largest_anagram(inputword):
    ##print "Input Letters: " + inputword
    for index in reversed(range(4,len(inputword)+1)):
        combos = itertools.combinations(inputword, index)
        for combo in combos:
            result = checkword(''.join(combo))
            if result != False:
                return result

    return set(["No Anagrams Found"])

def getDefnition(word):
    if(word.startswith("No Anagrams")):
        return ""
    import urllib
    import json
    url = "http://dictionaryapi.net/api/definition/%s" % word
    data = json.load(urllib.urlopen(url))
    try:
        result = str(data[0]['Definitions'])
        result = "Definition: " + result[3:-2]
        return result
    except:
        return "No definition found for '%s'" % word

#highest = find_largest_anagram(letter_generation.getLettersArray())

#print "Highest Anagram(s): " + str(highest)

#strhighest = highest.pop()

#print getDefnition(strhighest)

s = """\
from __main__ import find_largest_anagram
from __main__ import letter_generation
"""
if __name__ == '__main__':
    import timeit
    print (timeit.timeit("find_largest_anagram(letter_generation.getLettersArray())", setup=s, number=10000 ))
