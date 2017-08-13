import sys
from stemming.porter2 import stem

if __name__ == "__main__":

    [print("{}\t{}".format(word, stem(word))) for word in sys.argv]
