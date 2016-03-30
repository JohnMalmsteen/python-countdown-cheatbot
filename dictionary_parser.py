import letter_generation
import itertools

dictionary = dict()

file = open('words/354984si.ngl', 'r')
for line in file:
    line = line.strip()
    if len(line) > 3 and len(line) < 10 and line.isalpha() and line[0].islower():
        dictionary[''.join(sorted(line))] = line
file.close()

def checkword(inputword):
    if dictionary.has_key(''.join(sorted(inputword))):
        return dictionary[''.join(sorted(inputword))]
    else:
        return False

class Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def offer(self, elem):
        self.elements.insert(0, elem)

    def poll(self):
        return self.elements.pop()

    def count(self):
        return len(self.elements)


def find_largest_anagram(inputword):
    queue = Queue()
    print "Input Letters: " + inputword

    for index in reversed(range(3,len(inputword)+1)):
        map(queue.offer, itertools.combinations(inputword, index))

    while queue.isEmpty() == False:
        result = checkword(''.join(queue.poll()))
        if result != False:
            return result
    return "No Anagrams Found"


print "Highest Anagram: " + find_largest_anagram(letter_generation.getLettersArray())
