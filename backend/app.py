from flask import Flask, request, jsonify
import numpy as np
from joblib import load
from flask_cors import CORS
import pandas as pd
from preprocess import preprocess_csv


app = Flask(__name__)
CORS(app)

classifier = load("../ai_model/model.pkl")
anomaly_model = load("../ai_model/anomaly_model.pkl")

@app.route("/")
def home():
    return "AI Intrusion Detection System API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)

    attack_pred = classifier.predict(features)[0]
    anomaly_pred = anomaly_model.predict(features)[0]

    response = {
        "classification": "Attack" if attack_pred != 0 else "Normal",
        "anomaly": "Anomaly" if anomaly_pred == -1 else "Normal"
    }

    return jsonify(response)

@app.route("/stats")
def stats():
    return jsonify({
        "total_requests": 120,
        "attacks_detected": 34,
        "normal_traffic": 86
    })

if __name__ == "__main__":
    app.run(debug=True)
