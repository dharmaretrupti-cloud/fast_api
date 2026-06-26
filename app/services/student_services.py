# students = []

# def add_student(student):

#     students.append(student)

#     return student


# def get_students():

#     return students

from sqlalchemy.orm import Session
from app.models.student_model import StudentModel
from app.schemas.student_schemas import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = StudentModel(
        name=student.name,
        age=student.age
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(StudentModel).all()