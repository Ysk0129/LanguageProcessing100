
def read_morpheme_sentences(filename):

    with open(filename) as file:
        lines = [l.split("\t") for l in file.readlines()]
    
    all_morpheme_sentences = []
    sentence = []
    for line in lines:
        if len(line) >= 4:
            sentence.append({'surface': line[0], 'base': line[1], 'pos': line[2], 'pos1': line[3]})
            if line[3] == '記号-句点':
                all_morpheme_sentences.append(sentence)
                sentence = []

    return all_morpheme_sentences


if __name__ == "__main__":

    for sentence in read_morpheme_sentences("neko.txt.mecab"):
        print(sentence)
