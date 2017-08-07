import re

if __name__ == "__main__":
    with open("nlp.txt") as f:
        line = f.read()

    first = re.compile(r"[\.;:\?\!]")
    second = re.compile(r"\s")
    third = re.compile(r"[A-Z]")
    three_chars = []
    sentences = []
    sentence = ""
    for ch in line.replace("\n", ""):
        three_chars.append(ch)
        if len(three_chars) < 3:
            sentence += ch
            continue

        three_chars = three_chars[1:4]
        f = first.match(three_chars[0])
        s = second.match(three_chars[1])
        t = third.match(three_chars[1])
        if t is None or s is None or t is None:
            sentence += ch
        else:
            sentence.rstrip(" ")
            print(sentence)
            sentence = ""
