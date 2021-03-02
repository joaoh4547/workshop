from sklearn.neural_network import MLPClassifier


class NeuralNetwork:
    def __init__(self, n_layers=10):
        self.classifier = MLPClassifier(hidden_layer_sizes=n_layers)

    def train(self, X, labels):
        self.classifier.fit(X, labels)

    def test(self, X):
        return self.classifier.predict(X)
