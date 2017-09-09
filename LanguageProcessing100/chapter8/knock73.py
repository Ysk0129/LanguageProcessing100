import numpy as np
from stemming.porter2 import stem
from stopword import StopWord

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
    size = data_y.size
    hypothesis = sigmoid(data_x, theta)
    gradient = 1 / size * (hypothesis - data_y).dot(data_x)
    return gradient

def remove_stopword(stems):
    sw = StopWord()
    removed = [stm for stm in stems if not sw.is_included_stem(stm)]
    return removed

def make_dict_features(features):
    return {line: i for i, line in enumerate(features, start=1)}

def extract_included_features(stems, dict_features):
    data_x_element = np.zeros(len(dict_features) + 1, dtype=np.float64)
    #先頭要素は素性に対応しない重み用のため1とする
    data_x_element[0] = 1
    for stm in stems:
        if stm in dict_features.keys():
            data_x_element[dict_features[stm]] = 1
    return data_x_element

def learn(data_x, data_y, alpha, count):
    theta = np.zeros(data_x.shape[1])
    c = cost(data_x, theta, data_y)
    print("学習開始")
    print("cost: {}".format(c))

    for i in range(1, count + 1):
        g = gradient(data_x, theta, data_y)
        theta -= alpha * g

    c = cost(data_x, theta, data_y)
    print("学習完了")
    print("cost: {}".format(c))
    return theta

if __name__ == "__main__":

    features = load_features()
    sentiment_lines = load_sentiments()

    splited = [sentiment.split(" ") for sentiment in sentiment_lines]
    sentiments = [line[1:] for line in splited]

    #各行をそれぞれstemmingしたもの
    sentiments_stems = [stem_all(sentiment) for sentiment in sentiments]
    #正解ラベル
    labels = [line[0] for line in splited]

    dict_features = make_dict_features(features)

    data_x = np.zeros([len(sentiments_stems), len(dict_features) + 1], dtype=np.float64)
    data_y = np.zeros(len(labels), dtype=np.float64)

    for i, stems in enumerate(sentiments_stems):
        data_x[i] = extract_included_features(stems, dict_features)

        #labelの値が-1のときは0(デフォルト),+1のときは1とする
        #sentiments_stemsとlabelはsentimentsの1行に対応するので長さは同じ
        if labels[i] == "+1":
            data_y[i] = 1
    
    #学習率
    alpha = 6.0
    #学習の繰り返し数
    count = 1000
    theta = learn(data_x, data_y, alpha, count)

    np.save("theta.npy", theta)
