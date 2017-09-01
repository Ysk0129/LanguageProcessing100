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

def cost(data_x, theta, data_y):
    size = data_y.size
    hypothesis = sigmoid(data_x, theta)
    prediction = 1 / size * np.sum(-data_y * np.log(hypothesis) - (np.ones(size) - data_y) * np.log(np.ones(size) - hypothesis))
    return prediction

def gradient(data_x, theta, data_y):
    size = data_y.size()
    hypothesis = sigmoid(data_x, theta)
    gradient = 1 / size * (hypothesis - data_y).dot(data_x)
    return gradient
