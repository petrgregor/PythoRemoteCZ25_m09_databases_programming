"""Exercise 1
Use data in medical-data.json to create a new collection: medicaldata
- Find all rows with procedure_code equal 0F1F4ZC
- Find patient with patient_id equal 74, print his full name
- Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC
"""
import json

from connect_mongo import db_pr25

medical_col = db_pr25['medicaldata']

"""
with open('files/medical-data.json') as f:
    data = json.load(f)
    response = medical_col.insert_many(data)
    print(f"To collection 'medicaldata' were inserted {len(response.inserted_ids)} documents.")
"""

print("Find all rows with procedure_code equal 0F1F4ZC")
query = {'procedure_code': '0F1F4ZC'}
procedures = medical_col.find(query)
for procedure in procedures:
    print(procedure)

print('-'*80)
print("Find patient with patient_id equal 74, print his full name")
query = {'patient_id': 74}
patient = medical_col.find_one(query)
print(f"{patient['first_name']} {patient['last_name']}")

print('-'*80)
print("Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC")
query = {'visit_date.date': '2019-05-24T01:52:37.000Z'}
visits = medical_col.find(query)
for visit in visits:
    print(visit)

new_values = {'$set': {'procedure_code': '0F1F4ZC'}}
response = medical_col.update_many(query, new_values)
print(f"Number od updated documents: {response.modified_count}.")
visits = medical_col.find(query)
for visit in visits:
    print(visit)
