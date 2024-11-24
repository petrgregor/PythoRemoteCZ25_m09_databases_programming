from connect_db import session
from school_models import Student

student1 = Student(first_name="Adam", last_name="Bernau")
print(student1)
session.add(student1)
session.add(Student(first_name="Bedřich", last_name="Novák"))

students = [
    Student(first_name="Cyril", last_name="Svoboda"),
    Student(first_name="Dušan", last_name="Čermák"),
    Student(first_name="Eva", last_name="Svobodná"),
    Student(first_name="Filip", last_name="Černý")
]

#for student in students:
#    session.add(student)

session.add_all(students)

session.commit()
