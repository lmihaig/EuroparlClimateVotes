import pickle
import spacy

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


class Model:
    def __init__(self):
        vocabulary = pickle.load(open('trained_vect.pkl', 'rb'))
        self.vectorizer = CountVectorizer(decode_error='replace', vocabulary=vocabulary)
        self.nlp = spacy.load('en_core_web_lg')
        self.model = pickle.load(open('trained_model.pkl', 'rb'))

    def predict(self, x):
        '''Given text x, return if it is climate change related or not.'''
        lemmas = []
        tf_features = self.vectorizer.transform(x)
        return self.model.predict(x)