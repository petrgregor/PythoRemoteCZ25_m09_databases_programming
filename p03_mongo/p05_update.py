from connect_mongo import db_pr25

customer_collection = db_pr25['customers']

"""
myquery = {'surname': {'$exists': 0}}
for response in customer_collection.find(myquery):
    print(response)
print('-'*40)
print(customer_collection.find_one(myquery))

print('-'*40)
new_values = {'$set': {'surname': 'Moudrý'}}
customer_collection.update_one(myquery, new_values)

print(customer_collection.find_one({'name': 'Ivan'}))
"""

myquery = {'name': 'Helena', 'surname': 'Daniel'}
print(customer_collection.find_one(myquery))
new_value = {'$set':
                 {'surname': 'Danielová',
                  'address': 'Hnědá 15, Ostrava'
                  }
             }
customer_collection.update_one(myquery, new_value)

# update many
print('-'*80)
print("Všem zákazníků, z Ostravy přidáme informaci o kraji.")
myquery = {'address': {'$regex': 'Ostrava$'}}
for response in customer_collection.find(myquery):
    print(response)
new_value = {'$set': {'district': 'Moravskoslezský kraj'}}
response = customer_collection.update_many(myquery, new_value)
print(f"Bylo změněno {response.modified_count} záznamů.")
for response in customer_collection.find(myquery):
    print(response)
