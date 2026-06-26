from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.student_schemas import StudentCreate
from app.services.student_services import (
    create_student,
    get_students
)

router = APIRouter()

@router.post("/students")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)


@router.get("/students")
def read_students(db: Session = Depends(get_db)):
    return get_students(db)