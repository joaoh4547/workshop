import nltk
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from json import loads
from sklearn.model_selection import train_test_split
from ml.classifier import NeuralNetwork
from ml import pre_process_data, Tokenize
from utils import read_files_of_directory
from time import sleep


file_data = read_files_of_directory('data')

data = []
labels = []
for x in file_data:
    for k, i in x.items():
        for y in i:
            data.append(y)
            labels.append(k)
data = pre_process_data(data)

nn = NeuralNetwork()
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, train_size=0.9, shuffle=True)
tokenizer = Tokenize()
features = tokenizer.test_vectorizer(X_train)
nn.train(features, y_train)
app = Flask(__name__)
CORS(app)


@app.route('/classify', methods=['POST'])
def classifyText():
    body_data: dict = loads(request.data)
    if not body_data.get("text"):
        return jsonify({"message": "o texto é obrigatorio"}), 400
    text_features = tokenizer.transform([body_data['text']])
    pred = nn.test(text_features)
    sleep(5)
    return jsonify({"prediction": pred[0]}), 200


if __name__ == '__main__':
    app.run(debug=False, port=3000)
