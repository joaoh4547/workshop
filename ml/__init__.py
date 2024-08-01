from ml.features import pre_process_data
from ml.features import Tokenize
from ml.classifier import NeuralNetwork



# def Classify(text):
#     cw = load('model/classifier.model')
#     nn = NeuralNetwork(classifier=cw)
#     tokenizer = Tokenize()
#     tokenizer.load("model/data.voc")
#     features = tokenizer.transform([text])
#     print(features)
#     nn.test([features])


if __name__ == '__main__':
    pass
    # data = []
    # labels = []
    # for x in file_data:
    #     for k, i in x.items():
    #         for y in i:
    #             data.append(y)
    #             labels.append(k)
    # data = pre_process_data(data)
    # X_train, X_test, y_train, y_test = train_test_split(data, labels, train_size=0.9, shuffle=True)
    # tokenizer = Tokenize()
    # features = tokenizer.test_vectorizer(X_train)
#     # nn = NeuralNetwork(500)
#     # nn.train(features, y_train)
#     # nn.save()
#     # tokenizer.save()
#     # vectorizer = TfidfVectorizer(stop_words=stopwords.words("portuguese"), ngram_range=(1, 10))
#     # X_train_tfidf_vectorizer = vectorizer.fit_transform(X_train)
#     # knn.fit(X_train_tfidf_vectorizer, y_train)
#     # transformed = vectorizer.transform(X_test)
#     # predict = knn.predict(transformed)
#     # print(classification_report(y_test, predict))
#     # print(confusion_matrix(y_test, predict))
#     # term = "o presidente "
#     # term_tranf = vectorizer.transform([term])
#     # pr = knn.predict(term_tranf)[0]
