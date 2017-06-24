import knock30
import re

def count_occurrences_words(morphemes, **exclusions):

    word_occurrences_dict = {}
    for morpheme in morphemes:
        
        if "pos_list" in exclusions and morpheme["pos"] in exclusions["pos_list"]:
            continue
        if "condition" in exclusions and exclusions["condition"](morpheme["surface"]):
            continue

        if morpheme["surface"] in word_occurrences_dict.keys():
            word_occurrences_dict[morpheme["surface"]] += 1
        else:
            word_occurrences_dict[morpheme["surface"]] = 1

    return word_occurrences_dict

if __name__ == "__main__":

    morphemes = knock30.extract_morphemes("neko.txt.mecab")
    exclusion_pattern = re.compile("^[ぁ-ん]$")
    exclusion_func = lambda w: re.match(exclusion_pattern, w) is not None
    occurrences_dict = count_occurrences_words(morphemes, pos_list=["助詞", "助動詞", "記号"], condition=exclusion_func)
    
    for k, v in sorted(occurrences_dict.items(), key=lambda x: x[1], reverse=True):
        print(k + ":" + str(v))
