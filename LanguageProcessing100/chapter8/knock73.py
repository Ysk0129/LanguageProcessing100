
def load_features():
    with open("features.txt") as f:
        #語幹から改行を除去する
        lines = f.read().split("\n")
    return lines
