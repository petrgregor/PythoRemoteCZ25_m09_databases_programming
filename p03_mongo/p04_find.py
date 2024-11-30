from pymongo.errors import OperationFailure

from connect_mongo import db_pr25

import czech_sort

customers_collection = db_pr25["customers"]

print("Find one:")
response = customers_collection.find_one()
print(response)

print('-' * 80)
print("Find")
# SELECT * FROM customers;
for response in customers_collection.find():
    print(response)

print('-' * 80)
print("Find (pouze vybrané atributy)")
# SELECT name, surname FROM customers;
for response in customers_collection.find({}, {"_id": False, "name": True, "surname": 1}):
    print(response)

print('-' * 80)
print("Find (zakážeme některé atributy)")
# SELECT name, surname, phone_number FROM customers;
for response in customers_collection.find({}, {"_id": 1, "address": False, "email": 0}):
    print(response)

try:
    print('-' * 80)
    print("Find (chybně zadané atributy)")
    # SELECT name, surname FROM customers;
    for response in customers_collection.find({}, {"_id": 1, "address": 1, "email": 0}):
        print(response)
except OperationFailure as e:
    print(f"ERROR: {e}")
    print("Nefunguje kombinace 0/1 ve výběru atributů (kromě '_id')")

print('-' * 80)
print("Find (zakážeme _id)")
# SELECT * FROM customers;
for response in customers_collection.find({}, {"_id": 0}):
    print(response)

print('-' * 80)
print("Find (všechny zákazníky s příjmením 'Novák')")
myquery = {'surname': 'Novák'}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find({'surname': 'Novák'}):
    print(response)
print('-' * 40)
for response in customers_collection.find(myquery, {"_id": False, 'name': True, 'surname': True}):
    print(response)

print('-' * 80)
myquery = {'surname': {'$gt': 'N'}}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False, 'name': True, 'surname': True}):
    print(response)

print('-' * 80)
myquery = {'surname': {'$regex': '^N'}}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False, 'name': True, 'surname': True}):
    print(response)

print('-' * 80)
myquery = {'address': {'$regex': 'Praha$'}}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False}):
    print(response)

print('-' * 80)
myquery = {'surname': 'Svoboda', 'address': {'$regex': 'Praha$'}}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False}):
    print(response)

print('-' * 80)
myquery = {'name': {'$gte': 'C', '$lte': 'Gustav'}}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False}):
    print(response)

print('-' * 80)
print("Všichni zákazníci upořádaní podle příjmení (vzestupně)")
for response in customers_collection.find().sort("surname"):
    print(response)

print('-' * 80)
print("Všichni zákazníci upořádaní podle příjmení (sestupně)")
for response in customers_collection.find({}, {'_id': 0, 'name': 1, 'surname': 1, 'address': 1}).sort("surname", -1):
    try:
        print(f"name={response['name']}, surname={response['surname']}, address={response['address'][:10]}")
    except KeyError as e:
        print(f"ERROR: {e}")
        print(response)

"""FIXED: jak sortovat dle češtiny
V mongo lze nastavit kolekci:
customers_collection = db_pr25.create_collection(
    "customers",
    collation={
        "locale": "cs",  # Nastavení české lokalizace
        "strength": 1    # Ignoruje rozdíly mezi velkými a malými písmeny
    }
)
"""

print('-' * 80)
print("Všichni zákazníci uspořádaní dle adresy (vzestupně)")
for response in customers_collection.find({}, {'_id': 0}).sort('address'):
    print(response)

print('-' * 80)
print("Všichni zákazníci, kteří mají zadanou adresu")
myquery = {'address': {'$exists': "True"}}
for response in customers_collection.find(myquery, {'_id': 0}):
    print(response)

print('-' * 80)
print("Všichni záhazníci, kteří mají zadané jméno i příjmení")
myquery = {
    'name':
        {'$exists': 'True'},
    'surname':
        {'$exists': 'true'}
}
for response in customers_collection.find(myquery, {'_id': 0}):
    print(response)

print('-' * 80)
print("Všichni zákazníci bez zadané adresy")
myquery = {'address': {'$exists': False}}
for response in customers_collection.find(myquery, {'_id': 0}):
    print(response)

print('-' * 80)
print("Všichni zákazníci bez zadaného věku")
myquery = {'age': {'$exists': False}}
for response in customers_collection.find(myquery, {'_id': 0}):
    print(response)

print('-' * 80)
myquery = {
    'surname':
        {'$not':
             {'$regex': '^N'}
        }
}
print(f"Výsledek dotazu: {myquery}")
for response in customers_collection.find(myquery, {"_id": False, 'name': True, 'surname': True}):
    print(response)

print('-'*80)
print("První tři zákazníci (limit)")
myquery = {'surname': {'$exists': 1}}
for response in customers_collection.find(myquery, {'_id': 0}).sort('surname').limit(3):
    print(response)
