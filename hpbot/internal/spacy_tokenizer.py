import spacy
import os


class SpacyTokenizer:

    def __init__(self):
        self.tagger = spacy.load(os.environ['SPACY_PATH'])

    def tokenize(self, text):
        return [token.text for token in self.tagger(text)]
