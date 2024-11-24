from sqlalchemy_utils import database_exists, create_database

from connect_db import db
from school_models import Base

if not database_exists(db.url):
    create_database(db.url)  # creates database

Base.metadata.create_all(db)  # creates tables from classes in school_models.py
