
def load_features():
    with open("features.txt") as f:
        lines = f.read().split("\n")
    return lines
