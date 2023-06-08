import os
import pandas as pd
import tensorflow as tf
import gdown
import numpy as np
from flask import Flask, jsonify, request, redirect
from sklearn.preprocessing import MultiLabelBinarizer

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('model.h5')

# Load the label encoders
mlb = MultiLabelBinarizer()
# mlb.classes_ = np.load('label_encoder.npy', allow_pickle=True)

# Helper function to get the key from dictionary
def get_key(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    testype = data['testype']
    testopic = data['testopic']
    testopicsub = data['testopicsub']
    testdif = data['testdif']

    top_dict = {0: 'Back End', 1: 'Classification & Regression', 2: 'Computer Vision', 3: 'Data Engineering', 4: 'Front End', 5: 'NLP', 6: 'Speech / Audio', 7: 'Time-series'}
    subtop_dict = {0: 'ARIMA', 1: 'Angular', 2: 'Data Warehousing', 3: 'Django', 4: 'Ember.js', 5: 'Express.js', 6: 'LSTM', 7: 'Linear Regression', 8: 'Logistic Regression', 9: 'Music Information Retrieval', 10: 'Node.js', 11: 'Object Detection', 12: 'React', 13: 'Sentiment Analysis', 14: 'Speech Recognition', 15: 'Topic Modeling'}
    ptype_dict = {0: 'Back End', 1: 'Front End', 2: 'ML'}

    mlb =  [
    "Abdullah Nur Hudi",
    "Abiyyu Diora Haqi",
    "Alvin Tan",
    "Andhika Zulfikri",
    "Andi Rezal Oktavianto",
    "Azis Sofyanto",
    "Bagja Kurniadi",
    "Chairul Rizqi",
    "Christopher Kristianto",
    "Farel Eden",
    "Gabriel Kheisa",
    "I Putu Ranantha Nugraha Suparta",
    "Iga Narendra Pramawijaya",
    "Imam",
    "Muhammad Raden Syawali Akbar",
    "Nyoman Satiya Najwa Sadha",
    "Putu Gede Agung Karna Sampalan",
    "Rikip Ginanjar",
    "Sandrian Yulianto",
    "Sarah Sema Khairunisa",
    "Suci Rahmadani",
    "Vania Kylie",
    "Wahyu Fauzan"
    ]

    testX = [get_key(ptype_dict, testype)[0], get_key(top_dict, testopic)[0],
             get_key(subtop_dict, testopicsub)[0], testdif]
    testX = np.asarray([testX])
    yhat = model.predict(testX)[0]

    # Converting the prediction into dataframe
    predf = pd.DataFrame(yhat, index=mlb)
    predf = predf.multiply(100).round(0).sort_values(by=0, ascending=False)
    predf = predf[predf[0] >= 1]

    output = predf.to_dict(orient='index')

    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=int(os.environ.get("PORT", 8080)))
