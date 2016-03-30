import dictionary
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "", ["word="])
        result = dictionary.find_largest_anagram(args.pop())
        print result
        print dictionary.getDefnition(result.pop())
    except getopt.GetoptError:
        print 'countdown_solver.py <letters>'
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])
