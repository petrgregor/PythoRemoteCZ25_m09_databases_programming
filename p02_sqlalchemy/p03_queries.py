from sqlalchemy import text, and_, or_, desc

from connect_db import session, db
from school_models import Student


with db.connect() as conn:
    sql_statement = text("SELECT * FROM students;")
    results = conn.execute(sql_statement)
    for result in results:
        print(*result)

print('-'*80)
print("All students:")
students = session.query(Student).all()  # returns list of objects
print(f"students: {students}")
for student in students:
    print(student.full_name())

print('-'*80)
print("Count of students:")
total = session.query(Student).count()
print(f"Count: {total}")

print('-'*80)
print("Students with id > 3")
"""
SELECT * FROM students
WHERE students.id > 3;
"""
results = session.query(Student).filter(Student.id > 3)
print(results)
for result in results:
    print(result)

print('-'*80)
print("Students with last name starts with 'Svob':")
results = session.query(Student).filter(Student.last_name.like("Svob%"))
#print(results)
for result in results:
    print(result)

print('-'*80)
print("Students with id > 3 AND last name starts with 'Svob'")
#results = session.query(Student).filter(Student.id > 3, Student.last_name.like("Svob%"))
results = session.query(Student).filter(and_(Student.id > 3, Student.last_name.like("Svob%")))
for result in results:
    print(result)

print('-'*80)
print("Students with id > 3 OR last name starts with 'Svob'")
results = session.query(Student).filter(or_(Student.id > 3, Student.last_name.like("Svob%")))
for result in results:
    print(result)

print('-'*80)
print("Students with first name OR last name starts with 'B'")
results = session.query(Student).filter(or_(Student.first_name.like("B%"), Student.last_name.like("B%")))
#session.add(Student(first_name="Gusta", last_name="Beneš"))
#session.commit()
for result in results:
    print(result)
print('-'*40)
#session.add(Student(first_name="Helena", last_name="Budíková"))
#session.commit()
for result in results:
    print(result)

print('-'*80)
print("All students ordered by last_name:")
results = session.query(Student).order_by(Student.last_name)
for result in results:
    print(result)

print('-'*40)
#session.add(Student(first_name="Ivan", last_name="Novák"))
#session.commit()
for result in results:
    print(result)

print('-'*80)
print("All students ordered by last name and first name:")
results = session.query(Student).order_by(Student.last_name, Student.first_name)
for result in results:
    print(result)

print('-'*80)
print("All students ordered by last name (ascending) and first name (descending):")
results = session.query(Student).order_by(Student.last_name, desc(Student.first_name))
for result in results:
    print(result)

print('-'*80)
print("First three students (limit) ordered by last name (ascending) and first name (descending):")
results = session.query(Student).order_by(Student.last_name, desc(Student.first_name)).limit(3)
for result in results:
    print(result)

print('-'*80)
print("Exclude first three students (offset) ordered by last name (ascending) and first name (descending):")
results = session.query(Student).order_by(Student.last_name, desc(Student.first_name)).offset(3)
for result in results:
    print(result)

print('-'*80)
print("Fourth student ordered by last name (ascending) and first name (descending):")
results = session.query(Student).order_by(Student.last_name, desc(Student.first_name)).offset(3).limit(1)
for result in results:
    print(result)

print('-'*80)
print("First student ordered by last name (ascending):")
results = session.query(Student).order_by(Student.last_name).limit(1)  # list of one student
for result in results:
    print(result)
result = session.query(Student).order_by(Student.last_name).first()  # one student (one object)
#for r in result:
#    print(r)
#TypeError: 'Student' object is not iterable
print(result)

print('-'*80)
print("Student with id == 8:")
results = session.query(Student).filter(Student.id == 8)  # list
for result in results:
    print(result)
print('-'*40)
result = session.query(Student).get(8)  # one object
# LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
#   result = session.query(Student).get(8)  # one object
print(result)
