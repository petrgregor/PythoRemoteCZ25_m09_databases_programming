import os

from dotenv import load_dotenv

import pymongo

load_dotenv()

# vytvoření klienta
#mongo_client = pymongo.MongoClient("127.0.0.1", 27017)
#mongo_client = pymongo.MongoClient(os.getenv("mongo_host", default="127.0.0.1"),
#                                   int(os.getenv("mongo_port", default=27017)))
# nebo
#mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mongo_client = pymongo.MongoClient(f"mongodb://{os.getenv("mongo_host", default="127.0.0.1")}:"
                                   f"{os.getenv("mongo_port", default=27017)}")

# vytvoření databáze
db_test25 = mongo_client.db_test25
# nebo
db_pr25 = mongo_client["PythonRemoteCZ25"]


if __name__ == '__main__':
    print(f"mongo_client: {mongo_client}")
    print(f"db_test25: {db_test25}")
    print(f"db_pr25: {db_pr25}")

    databases = mongo_client.list_database_names()
    print(f"databases: {databases}")

    # vytvoření kolekce ("tabulka")
    customer_collection = db_pr25["customers"]
