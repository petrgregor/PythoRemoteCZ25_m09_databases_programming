import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from p01_mysql.connection_details import *

load_dotenv()

#CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/cinematic2"
#db = create_engine(CONNECTION_STRING.format(user=os.getenv("user", default="test"),
#                                            password=os.getenv("password", default="test"),
#                                            host=os.getenv("host", default="localhost"),
#                                            port=os.getenv("port", default=3306)))

db = create_engine(f"mysql+mysqlconnector://{os.getenv("user", default="test")}:"
                   f"{os.getenv("password", default="test")}@"
                   f"{os.getenv("host", default="localhost")}:"
                   f"{os.getenv("port", default=3306)}"
                   f"/school")

Session = sessionmaker(bind=db)
session = Session()

print(f"db.url = {db.url}")

