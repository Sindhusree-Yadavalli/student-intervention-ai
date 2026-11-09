from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Student Intervention AI"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Student AI Running"
    }