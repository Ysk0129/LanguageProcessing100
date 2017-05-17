from random import shuffle

def typoglycemia(txt):
    words= txt.split()
    sentence = []

    for word in words:
        if len(word) > 4:
            middle = list(word[1:-1])
            shuffle(middle)
            shuffled = "".join(list(word[0]) + middle + list(word[-1]))
            sentence.append(shuffled)
        else:
            sentence.append(word)

    return " ".join(sentence)


if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    answer = typoglycemia(text)

    print(answer)
