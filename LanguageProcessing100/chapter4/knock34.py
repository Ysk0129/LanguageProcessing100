import sys
sys.path.append('../')
from chapter1.knock05 import create_ngram
import knock30

def search_concatenated(concatenation_str, pos, morphemes):

    trigram  = create_ngram(morphemes, 3)
    concatenated = []
    for group in trigram:
        if group[1]["surface"] == concatenation_str and group[0]["pos"] == pos and group[2]["pos"] == pos:
            concatenated.append([group[0]["surface"] + group[1]["surface"] + group[2]["surface"]])

    return concatenated


if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    print(search_concatenated("の", "名詞", morphemes))
