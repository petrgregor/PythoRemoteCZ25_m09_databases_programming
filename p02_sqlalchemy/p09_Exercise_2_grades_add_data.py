"""Exercise 2
● Add some grades for each student
"""
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from school_models import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Grade(student=1, grade=2, date_created=datetime(2024, 11, 14, 14, 28)),
            Grade(student=2, grade=1, date_created=datetime(2024, 11, 15, 15, 28)),
            Grade(student=8, grade=3, date_created=datetime(2024, 11, 16, 7, 28)),
            Grade(student=6, grade=2, date_created=datetime(2024, 11, 18, 8, 28)),
            Grade(student=5, grade=1, date_created=datetime(2024, 11, 19, 10, 28)),
            Grade(student=1, grade=2, date_created=datetime(2024, 11, 20, 11, 28)),
            Grade(student=2, grade=4, date_created=datetime(2024, 11, 20, 12, 28)),
            Grade(student=10, grade=3, date_created=datetime(2024, 11, 21, 13, 28)),
            Grade(student=6, grade=1, date_created=datetime(2024, 11, 22, 10, 28)),
            Grade(student=2, grade=1, date_created=datetime(2024, 11, 22, 11, 28)),
            Grade(student=3, grade=1, date_created=datetime(2024, 11, 23, 12, 28)),
            Grade(student=5, grade=2, date_created=datetime(2024, 11, 23, 13, 28)),
            Grade(student=2, grade=3, date_created=datetime(2024, 11, 24, 7, 28)),
            Grade(student=1, grade=3, date_created=datetime(2024, 11, 24, 8, 28)),
            Grade(student=2, grade=1, date_created=datetime(2024, 11, 24, 9, 28)),
            Grade(student=1, grade=2, date_created=datetime(2024, 11, 24, 14, 28))
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(e)
