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


class Address(Base):
    """Exercise 1
    ● Create a new table called address
    ● It should include the following fields:
        ○ student int, foreign key, primary key
        ○ street_name string
        ○ number int
        ○ city string"""
    __tablename__ = "address"
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)
    street_name = Column(String(50))
    number = Column(Integer)
    city = Column(String(50))

    def __repr__(self):
        return (f"Address(student={self.student}, "
                f"street_name={self.street_name}, "
                f"number={self.number}, "
                f"city={self.city})")

    def __str__(self):
        return f"Address: {self.street_name} {self.number}, {self.city}"
