import joblib

model = joblib.load(
    "app/ml/model.pkl"
)

def predict_risk(
    attendance,
    mathematics,
    science,
    english
):

    prediction = model.predict([
        [
            attendance,
            mathematics,
            science,
            english
        ]
    ])

    return prediction[0]