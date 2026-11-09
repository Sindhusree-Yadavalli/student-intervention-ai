import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("../dataset/student_dataset.csv")

X = df[
    [
        "attendance",
        "mathematics",
        "science",
        "english"
    ]
]

y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(
    model,
    "app/ml/model.pkl"
)

print("Model Trained Successfully")