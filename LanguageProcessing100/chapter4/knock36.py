import knock30
import re

def count_occurrences_words(morphemes, exclusion_pos_list, exclusion_condition):

    word_occurrences_dict = {}
    for morpheme in morphemes:

        if morpheme["pos"] in exclusion_pos_list:
            continue
        if exclusion_condition(morpheme["surface"]):
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
    word_occurrences_dict = count_occurrences_words(morphemes, ["助詞", "助動詞", "記号"], exclusion_func)

    for k, v in sorted(word_occurrences_dict.items(), key=lambda x: x[1], reverse=True):
        print(k + ":" + str(v))
