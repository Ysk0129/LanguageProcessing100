import re

if __name__ == "__main__":
    with open("nlp.txt") as f:
        line = f.read()

    first = re.compile(r"[.;:?!]")
    second = re.compile(r"\s")
    third = re.compile(r"[A-Z]")
    three_chars = []
    sentence = ""

    for ch in line.replace("\n", " ").replace("\t", " "):

        three_chars.append(ch)

        if len(three_chars) < 3:
            continue

        if len(three_chars) > 3:
            three_chars = three_chars[1:4]

        if three_chars[1] == " " and three_chars[2] == " ":
            three_chars = three_chars[0:3]
            continue

        f = first.match(three_chars[0])
        s = second.match(three_chars[1])
        t = third.match(three_chars[2])

        if f is None or s is None or t is None:
            sentence += ch
        else:
            sentence.rstrip(" ")
            print(sentence)
            sentence = ch
