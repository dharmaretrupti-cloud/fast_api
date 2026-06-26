from sqlalchemy import Column, Integer, String
from app.database.db import Base

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    