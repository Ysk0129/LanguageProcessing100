import sys
import re

if __name__ == "__main__":

    sentences = sys.argv[1].split("\n")
    for sentence in sentences:
        words = sentence.split(" ")
        for i in range(0, len(words)):
            print(words[i])
            if i == len(words) -1:
                print()
