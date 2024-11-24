"""Exercise 2
● Print out all grades per each student using filter"""
from sqlalchemy import func

from connect_db import session
from school_models import *

print("Print out all grades per each student using filter (sorted by last name and first name)")
results = session.query(Student, Grade).join(Grade).order_by(Student.last_name, Student.first_name)
for student, grade in results:
    print(f"{student.full_name()}: {grade.grade}")

print('-'*80)
print("all students and all their grades:")
students = session.query(Student).order_by(Student.last_name, Student.first_name)
for student in students:
    print(f"{student.full_name()}:")
    grades = session.query(Grade).filter(Grade.student == student.id).order_by(Grade.date_created)
    for grade in grades:
        print(f"\t{grade.grade} ({grade.date_created})")
    if grades.count() == 0:
        print("\tNo grades.")

print('-'*80)
print("number of grades for each student")
for student in students:
    grades = session.query(Grade).filter(Grade.student == student.id).count()
    if grades == 0:
        print(f"{student.full_name()} has no grade.")
    elif grades == 1:
        print(f"{student.full_name()} has {grades} grade.")
    else:
        print(f"{student.full_name()} has {grades} grades.")

print('-'*80)
print("number of grades for each student using aggregation function")
results = (session.query(Student, func.count(Grade.id))
           .join(Grade)
           .group_by(Student.id)
           .order_by(Student.last_name, Student.first_name))
for student, grades in results:
    if grades == 0:  # warning: by aggregation function there is no student without grades in results!
        print(f"{student.full_name()} has no grade.")
    elif grades == 1:
        print(f"{student.full_name()} has {grades} grade.")
    else:
        print(f"{student.full_name()} has {grades} grades.")

print('-'*80)
print("average grade for each student")
averages = (session.query(Student, func.avg(Grade.grade))
            .join(Grade)
            .group_by(Student.id)
            .order_by(Student.last_name, Student.first_name))
for student, average in averages:
    print(f"{student.full_name()} has average grade {round(average, 2)}.")
    # Warning: there is no student without grades in results.

print('-'*80)
print("best student (with lowest average grade)")
best_student, average = min(averages, key=lambda x: x[1])
print(f"Best student is {best_student.full_name()} with average grade {round(average, 2)}.")

print('-'*80)
print("delete the oldest grade")
oldest_grade = session.query(Grade).order_by(Grade.date_created).first()
print(oldest_grade)
session.delete(oldest_grade)
session.commit()
