
def create_ngram(sequence, n):
    ngram = [sequence[i:i+n] for i in range(len(sequence) - n + 1)]
    return ngram

if __name__ == "__main__":
    sentence = "I am an NLPer"

    char_bigram = create_ngram(sentence.replace(" ", ""), 2)
    print(char_bigram)

    word_bigram = create_ngram(sentence.split(), 2)
    print(word_bigram)
