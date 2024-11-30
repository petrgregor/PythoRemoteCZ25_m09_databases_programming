from pymongo.errors import OperationFailure

from connect_mongo import db_pr25, mongo_client

customers_collections = db_pr25["customers"]

try:
    with mongo_client.start_session() as session:
        with session.start_transaction():
            response = customers_collections.insert_one({"_id": 10, "name": "Karla"}, session=session)
            print(f"last inserted id: {response.inserted_id}")
            response = customers_collections.insert_one({"_id": 1, "name": "Lukáš"}, session=session)
            print(f"last inserted id: {response.inserted_id}")
except OperationFailure as e:
    print(f"ERROR: {e}")
except NameError as e:
    print(f"ERROR: {e}")

try:
    with mongo_client.start_session() as session:
        with session.start_transaction():
            customers = [
                {"name": "Kamil", "surname": "Dvořák"},
                {"_id": 3, "name": "Lucie", "surname": "Výborná"}
            ]
            response = customers_collections.insert_many(customers, session=session)
            print(f"last inserted ids: {response.inserted_id}")
except OperationFailure as e:
    print(f"ERROR: {e}")
except NameError as e:
    print(f"ERROR: {e}")

try:
    response = customers_collections.insert_one({"_id": 10, "name": "Karla", "phone_number": "+420777123456"})
    print(f"last inserted id: {response.inserted_id}")
except OperationFailure as e:
    print(f"ERROR: {e}")
except NameError as e:
    print(f"ERROR: {e}")

print("END")
