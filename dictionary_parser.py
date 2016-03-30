import letter_generation
import itertools



def checkword(inputword):
    file = open('words/354984si.ngl', 'r')
    inputword = ''.join(sorted(inputword))
    for line in file:
        line = line.strip()
        if len(line) > 3 and len(line) < 10 and line.isalpha() and line[0].islower():
            if ''.join(sorted(line)) == inputword:
                file.close()
                return True
    file.close()
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

    for index in reversed(range(4,len(inputword)+1)):
        map(queue.offer, itertools.combinations(inputword, index))

    while queue.isEmpty() == False:
        print checkword(''.join(queue.poll()))


find_largest_anagram("aardvark")
