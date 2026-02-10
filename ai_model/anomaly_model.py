from sklearn.ensemble import IsolationForest
from joblib import dump
from preprocess import load_and_preprocess

X, y = load_and_preprocess("dataset/KDDTrain+.txt")

# Train only on normal traffic (label = 0)
normal_data = X[y == 0]

anomaly_model = IsolationForest(contamination=0.1)
anomaly_model.fit(normal_data)

dump(anomaly_model, "anomaly_model.pkl")
print("✅ Anomaly detection model saved")
