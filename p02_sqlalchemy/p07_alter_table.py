from sqlalchemy import text

from connect_db import db

#from school_models import Student, Base

# Base.metadata.create_all(db)  #dosn't work
with db.connect() as conn:
    sql_statement = text("ALTER TABLE students ADD class_name VARCHAR(30);")
    conn.execute(sql_statement)
