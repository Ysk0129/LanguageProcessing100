import re

def read_morpheme_sentences(filename):

    with open(filename) as file:
        lines = [l.split("\t") for l in file.readlines()]
    
    all_morpheme_sentences = []
    sentence = []
    pos_pattern = re.compile(r"^(.*?)\-(.*?)$")
    
    for line in lines:
        if len(line) >= 4:
            search_result = re.search(pos_pattern, line[3])
            if search_result is not None:
                pos = search_result.group(1)
                pos1 = search_result.group(2)
            else:
                pos = line[3]
                pos1 = line[3]
                print(line)

            sentence.append({"surface": line[0], "base": line[1], "pos": pos, "pos1": pos1})
            if pos1 == "句点":
                all_morpheme_sentences.append(sentence)
                sentence = []

    return all_morpheme_sentences


if __name__ == "__main__":

    for sentence in read_morpheme_sentences("neko.txt.mecab"):
        print(sentence)
