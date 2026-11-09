from fastapi import APIRouter
from pydantic import BaseModel
from app.services.predictor import predict_risk

router = APIRouter()


class Student(BaseModel):
    attendance: float
    mathematics: float
    science: float
    english: float


def get_recommendation(student):

    recommendations = []

    if student.attendance < 75:
        recommendations.append("Parent Meeting")

    if student.mathematics < 50:
        recommendations.append("Math Tutoring")

    if student.science < 50:
        recommendations.append("Science Support")

    if student.english < 50:
        recommendations.append("English Coaching")

    return recommendations


@router.post("/predict")
def predict(student: Student):

    risk = predict_risk(
        student.attendance,
        student.mathematics,
        student.science,
        student.english
    )
    return {
    "attendance": student.attendance,
    "mathematics": student.mathematics,
    "science": student.science,
    "english": student.english,
    "risk": risk,
    "recommendations": get_recommendation(student)
}