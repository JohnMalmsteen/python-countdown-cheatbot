import letter_generation
file = open('words/354984si.ngl', 'r')

def checkword(inputword):
    inputword = ''.join(sorted(inputword))
    for line in file:
        line = line.strip()
        if len(line) > 3 and len(line) < 10 and line.isalpha() and line[0].islower():
            if ''.join(sorted(line)) == inputword:
                return True
    return False

print checkword('aarvarkdsz')
