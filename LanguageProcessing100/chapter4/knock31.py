import knock30

def search_morphemes(morphemes, extract_target_key, search_key, condition_value):

    return [morpheme[extract_target_key] for morpheme in morphemes if morpheme[search_key] == condition_value]


if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    verbs_surface = search_morphemes(morphemes, "surface", "pos", "動詞")
    print(verbs_surface)
