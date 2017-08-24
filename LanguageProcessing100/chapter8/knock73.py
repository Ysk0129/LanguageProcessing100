import numpy as np

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
