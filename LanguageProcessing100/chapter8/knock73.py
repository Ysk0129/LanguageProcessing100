
def load_features():
    with open("features.txt") as f:
        #語幹から改行を除去する
        lines = f.read().split("\n")
    return lines

def load_sentiments():
    with open("sentiment.txt") as f:
        #改行を除去する
        lines = f.read().split("\n")
    return lines
