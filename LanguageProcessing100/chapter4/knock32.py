import knock30, knock31

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    verbs_base = knock31.search_morphemes(morphemes, "base", "pos", "動詞")
    print(verbs_base)
