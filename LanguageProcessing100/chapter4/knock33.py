import knock30, knock31

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    nouns_sa = knock31.search_morphemes(morphemes, "surface", "pos1", "サ変接続")
    print(nouns_sa)
