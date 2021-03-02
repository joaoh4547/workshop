import re
from unicodedata import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from joblib import dump, load


def pre_process_data(data):
    new_data = []
    for i in data:
        text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', i)
        txt2 = re.sub(r'[!-,.:-@]|(?<![a-záéíóúâêôãõç])-|-(?![a-záéíóúâêôãõç])', '', text)
        new_data.append(normalize('NFKD', txt2).encode('ASCII', 'ignore').decode('ASCII'))
    return new_data


class Tokenize:
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("portuguese"), ngram_range=(1, 10))

    def test_vectorizer(self, data):
        return self.vectorizer.fit_transform(data)

    def transform(self, data):
        return self.vectorizer.transform(data)

    def save(self):
        dump(self.vectorizer, 'model/data.voc')

    def load(self, path):
        voc = load(path)
        print(voc)
        self.vectorizer = voc
