import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_csv(file):
    df = pd.read_csv(file)

    # Encode categorical columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    scaler = StandardScaler()
    X = scaler.fit_transform(df)

    return X
