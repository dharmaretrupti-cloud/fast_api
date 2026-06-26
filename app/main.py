from fastapi import FastAPI

from app.database.db import engine, Base
from app.routes.student_routes import router
from app.database.db import Base, engine
from app.models.student_model import StudentModel

StudentModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "FastAPI PostgresSQL Working"}