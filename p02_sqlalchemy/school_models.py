from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
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


class Grade(Base):
    """Exercise 2
    ● Create a table called grades
    ● It should include the following fields:
        ○ id int, primary key, autoincrement
        ○ student int, foreign key
        ○ grade int or string - whichever you prefer
        ○ date_created datetime"""
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id), nullable=False)
    grade = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __repr__(self):
        return (f"Grade(id={self.id}, "
                f"student={self.student}, "
                f"grade={self.grade}, "
                f"date_created={self.date_created})")

    def __str__(self):
        return f"Student {self.student} has grade {self.grade} ({self.date_created}) #{self.id}"
