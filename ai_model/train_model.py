from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from preprocess import load_and_preprocess

X, y = load_and_preprocess("dataset/KDDTrain+.txt")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

dump(model, "model.pkl")
print("✅ Classification model saved")
