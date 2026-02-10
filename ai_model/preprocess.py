import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path):
    df = pd.read_csv(path, header=None)

    # Label column
    df.rename(columns={41: "label"}, inplace=True)

    # Encode categorical columns
    for col in df.select_dtypes(include="object").columns:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

    X = df.drop("label", axis=1)
    y = df["label"]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y
