from connect_mongo import db_pr25

customers_collection = db_pr25['customers']

myquery = {'name': 'Gustav', 'surname': 'Novák'}
for response in customers_collection.find(myquery):
    print(response)
customers_collection.delete_one(myquery)
for response in customers_collection.find(myquery):
    print(response)

print('-'*80)
print("Smažeme všechny zákazníky z Ostravy")
myquery = {'address': {'$regex': 'Ostrava$'}}
for response in customers_collection.find(myquery):
    print(response)
response = customers_collection.delete_many(myquery)
print(f"Bylo smazáno {response.deleted_count} záznamů.")
for response in customers_collection.find(myquery):
    print(response)

print('-'*80)
print("Smažeme všechny zákazníky")
response = customers_collection.delete_many({})
print(f"Bylo smazáno {response.deleted_count} záznamů.")

print('-'*80)
print("Smažeme celou kolekci")
customers_collection.drop()
