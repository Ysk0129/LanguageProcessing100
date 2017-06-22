import knock30

def extract_consecutive(pos, morphemes):

    consecutive = []
    all_consecutive = []
    for morpheme in morphemes:
        if morpheme["pos"] != pos:
            if consecutive != [] and len(consecutive) >= 2:
                all_consecutive.append(consecutive)
            consecutive = []
        else:
            consecutive.append(morpheme["surface"])

    return all_consecutive

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    print(extract_consecutive("名詞", morphemes))
