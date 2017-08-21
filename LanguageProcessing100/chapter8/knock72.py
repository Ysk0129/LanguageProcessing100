import re
from stopword import StopWord
from stemming.porter2 import stem

def trim_ignore_marks(word):
    ignore_marks = re.compile(r"[^a-zA-Z!?']")
    return re.sub(ignore_marks, "", word)

def preprocess_stems(stems):
    sw = StopWord()
    return [trim_ignore_marks(stm) for stm in stems if not sw.is_included_stem(stm)]

if __name__ == "__main__":

    with open("sentiment.txt") as f:
        lines = f.readlines()

    words_list = [line.split(" ")[1:] for line in lines]
    #flatten
    words = [word for words in words_list for word in words]
    #stemming処理に時間がかかるため、stemmingしない状態で先にuniqにする
    uniq_words = list(set(words))
    stems = [stem(word) for word in uniq_words]

    features = list(set(preprocess_stems(stems)))
    features.remove("")

    with open("features.txt", "w") as f:
        f.writelines("\n".join(features))
