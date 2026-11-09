import pandas as pd
import random

data = []

for i in range(1000):

    attendance = random.randint(40, 100)
    mathematics = random.randint(30, 100)
    science = random.randint(30, 100)
    english = random.randint(30, 100)

    avg = (mathematics + science + english) / 3

    if attendance < 60 or avg < 50:
        risk = "high"
    elif attendance < 75:
        risk = "medium"
    else:
        risk = "low"

    data.append(
        [
            attendance,
            mathematics,
            science,
            english,
            risk
        ]
    )

df = pd.DataFrame(
    data,
    columns=[
        "attendance",
        "mathematics",
        "science",
        "english",
        "risk"
    ]
)

df.to_csv(
    "../dataset/student_dataset.csv",
    index=False
)

print(df.head())

print("Dataset Generated Successfully")