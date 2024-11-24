from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    class_name = Column(String(30))

    def __repr__(self):
        return f"Student(first_name={self.first_name}, last_name={self.last_name})"

    def __str__(self):
        return f"Student #{self.id} {self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Locker(Base):
    __tablename__ = "lockers"
    number = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey(Student.id))

    def __repr__(self):
        return f"Locker(number={self.number}, student={self.student})"

    def __str__(self):
        return f"Locker #{self.number} belongs to student: {self.student}"
