from sqlalchemy.exc import IntegrityError

from connect_db import db, session
from school_models import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Locker(number=1, student=5),
            Locker(number=2, student=6),
            Locker(number=3, student=10),
            Locker(number=4, student=8),
            Locker(number=5, student=1),
            Locker(number=6, student=6),
            Locker(number=7)
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(e)
