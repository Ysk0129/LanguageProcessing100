import sys
import re

if __name__ == "__main__":

    term = re.compile(r"[,;:?!\(\)\"]")
    dot = re.compile(r"\.")

    sentences = sys.argv[1].split("\n")
    for sentence in sentences:
        words = sentence.split(" ")
        for i in range(0, len(words)):
            words[i] = re.sub(term, "", words[i])
            if len(words[i]) > 0 and re.match(dot, words[i][-1]) is not None:
                words[i] = words[i][:-1]
            print(words[i])
            if i == len(words) -1:
                print()
