from connect_db import session
from school_models import *

print("Join students with their lockers, print students owning locker:")
results = session.query(Student).join(Locker)
print(results)
for result in results:
    print(result)

print('-'*80)
print("Join students with their lockers, print students with their locker sorted by locker number:")
results = session.query(Student, Locker.number).join(Locker).order_by(Locker.number)
print(results)
for result in results:
    print(result)
print('-'*40)
for result in results:
    student, locker_number = result
    print(f"Locker #{locker_number}: {student}")

print('-'*80)
print("Student with locker #4:")
results = session.query(Student).join(Locker).filter(Locker.number == 4)
for result in results:
    print(result)
