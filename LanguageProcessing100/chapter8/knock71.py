import unittest
from stopword import StopWord

class StopWordTest(unittest.TestCase):

    def test_is_included_true(self):
        stopwords = ["a", "did", "in", "only", "then", "where", "all", "do", "into", "onto", "there", "whether",
            "almost", "does", "is", "or", "thereforet", "which", "also", "either", "it", "our", "these", "while",
            "although", "for", "its", "ours", "they", "who", "an", "from", "just", "s", "this", "whose",
            "and", "had", "ll", "shall", "those", "why", "any", "has", "me", "she", "though", "will",
            "are", "have", "might", "should", "through", "with", "as", "having", "Mr", "since", "thus", "would",
            "at", "he", "Mrs", "so", "to", "yet", "be", "her", "Ms", "some", "too", "you",
            "because", "here", "my", "still", "until", "your", "been", "hers", "no", "such", "ve", "yours",
            "both", "him", "non", "t", "very", "but", "his", "nor", "than", "was", 
            "by", "how", "not", "that", "we", "can", "however", "of", "the", "were",
            "could", "i", "on", "their", "what", "d", "if", "one", "them", "when"]

        sw = StopWord()

        for stopword in stopwords:
            result = sw.is_included(stopword)
            self.assertTrue(result)

    def test_is_included_false(self):
        not_stopwords = ["dog", "cat", "python", "pip", "install", "requests", "array", "whenever", ""]

        sw = StopWord()

        for not_stopword in not_stopwords:
            result = sw.is_included(not_stopword)
            self.assertFalse(result)
        return 0

if __name__ == "__main__":
    unittest.main()
