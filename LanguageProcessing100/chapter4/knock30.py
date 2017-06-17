import re

def extract_morphemes(filename):

    with open(filename) as file:
        lines = [l.split("\t") for l in file.readlines()]
    
    morphemes = []
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
            morphemes.append({"surface": line[0], "base": line[2], "pos": pos, "pos1": pos1})

    return morphemes

def separate_morphemes_with_sentence(morphemes):

    all_morpheme_sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)

        if morpheme["pos1"] == "句点":
            all_morpheme_sentences.append(sentence)
            sentence = []
    
    return all_morpheme_sentences


if __name__ == "__main__":

    morphemes = extract_morphemes("neko.txt.mecab")
    sentenses = separate_morphemes_with_sentence(morphemes)

    for sentence in sentenses:
        print(sentence)
