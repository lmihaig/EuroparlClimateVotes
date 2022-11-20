import pickle
import spacy
from sklearn.feature_extraction.text import CountVectorizer


class Model:
    def __init__(self):
        vocabulary = pickle.load(open('trained_vect.pkl', 'rb'))
        self.vectorizer = CountVectorizer(decode_error='replace', vocabulary=vocabulary)
        # e nevoie de $python -m spacy download en_core_web_sm
        self.nlp = spacy.load('en_core_web_sm')
        self.model = pickle.load(open('trained_model.pkl', 'rb'))

    def predict(self, text):
        '''Given a text, return if it is climate change related or not.'''
        processed_text = self.nlp(text)
        lemmas = ' '.join([token.lemma_ for token in processed_text])
        tf_features = self.vectorizer.transform([lemmas])
        return bool(self.model.predict(tf_features)[0])
