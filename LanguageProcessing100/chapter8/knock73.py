import numpy as np
from stemming.porter2 import stem

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

def sigmoid(data_x, theta):
    print(np.exp(-data_x.dot(theta)))
    return 1 / (1 + np.exp(-data_x.dot(theta)))

def stem_all(words):
    stems = [stem(word) for word in words]
    return stems
