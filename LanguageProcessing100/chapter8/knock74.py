import numpy as np
import unittest
import knock73

class PredictionTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(PredictionTest, self).__init__(*args, **kwargs)
        features = knock73.load_features()
        self.dict_features = knock73.make_dict_features(features)
        self.theta = np.load("theta.npy")
        self.threshold = 0.5

    def test_predict_negative(self):
        sentence = "It was a very unpleasant movie, so I do not want to see it anymore !"
        negative_data = self.make_data(sentence)
        result = knock73.sigmoid(negative_data, self.theta)
        print("Predicted value of negative sentence: {}".format(result))
        self.assertLess(result, self.threshold)

    def test_predict_positive(self):
        sentence = "This is a very wonderful movie. I want to see it again ."
        positive_data = self.make_data(sentence)
        result = knock73.sigmoid(positive_data, self.theta)
        print("Predicted value of positive sentence: {}".format(result))
        self.assertGreaterEqual(result, self.threshold)

    def make_data(self, sentence):
        stems = knock73.stem_all(sentence.split(" "))
        return knock73.extract_included_features(stems, self.dict_features)

if __name__ == "__main__":
    unittest.main()
