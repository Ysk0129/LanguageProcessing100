import numpy as np
import knock73

if __name__ == "__main__":
    theta = np.load("theta.npy")
    features = knock73.load_features()

    index_sorted = np.argsort(theta)

    print("top 10")
    for i in index_sorted[:-11:-1]:
        t = theta[i]
        f = features[i - 1]
        print("{} : {}".format(t, f))

    print("worst 10")
    for i in index_sorted[:10]:
        t = theta[i]
        f = features[i - 1]
        print("{} : {}".format(t, f))
