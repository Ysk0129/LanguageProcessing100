import sys

if __name__ == "__main__":

    sentences = sys.argv[1].split("\n")
    for sentence in sentences:
        words = sentence.split("\s")
        for word in words:
            print(word)
