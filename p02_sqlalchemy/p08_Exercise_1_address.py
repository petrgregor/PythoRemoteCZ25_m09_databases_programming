"""Exercise 1
● Add an Address for each student
● Print out all students along with their addresses using a join()"""
from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from school_models import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Address(student=1, street_name="Hlavní", number=5, city="Brno"),
            Address(student=2, street_name="Vedlejší", number=8, city="Brno"),
            Address(student=3, street_name="Jarní", number=15, city="Ostrava"),
            Address(student=4, street_name="Letní", number=7, city="Brno"),
            Address(student=5, street_name="Podzimní", number=3, city="Olomouc"),
            Address(student=6, street_name="Zimní", number=9, city="Brno"),
            Address(student=8, street_name="Náměstí Svobody", number=25, city="Jihlava"),
            Address(student=10, street_name="Nábřeží", number=25, city="Praha")
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(e)

print("Print out all students along with their addresses using a join()")
results = session.query(Student, Address).join(Address)
for student, address in results:
    print(f"{student}: {address}")

print('-'*80)
print("all students from Brno")
results_Brno = session.query(Student, Address).join(Address).filter(Address.city == 'Brno')
for student, address in results_Brno:
    print(f"{student}: {address}")

print('-'*80)
print("all students from Brno sorted alphabetically by last_name")
results_Brno_sorted = results_Brno.order_by(Student.last_name)
for student, address in results_Brno_sorted:
    print(f"{student}: {address}")

print('-'*80)
print("change street_name and number to 'Vedlejší 7' for student 'Adam Bernau'")
student, address = session.query(Student, Address).join(Address).filter(Student.first_name == 'Adam', Student.last_name == 'Bernau').first()
print(f"{student}: {address}")
address.street_name = "Vedlejší"
address.number = 7
session.commit()
print(f"{student}: {address}")
