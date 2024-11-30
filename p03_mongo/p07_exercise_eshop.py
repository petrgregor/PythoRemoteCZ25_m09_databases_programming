"""E-shop
Kolekce:
1. Customers (id, name, surname, address)
2. Storage (id, product, serial_number, count)
3. Order (id, Customer, Product, count)
"""

from connect_mongo import db_pr25

customers_col = db_pr25['customers']
storage_col = db_pr25['storage']
order_col = db_pr25['order']

customers = [
    {'name': 'Aleš', 'surname': 'Hodný', 'address': {'street': 'Hlavní', 'number': 25, 'city': 'Praha'}},
    {'name': 'Bohumil', 'surname': 'Zlý', 'address': {'street': 'Vedlejší', 'number': 2, 'city': 'Ostrava'}},
    {'name': 'Ctibor', 'surname': 'Ošklivý', 'address': {'street': 'Jarní', 'number': 7, 'city': 'Brno'}}
]

products = [
    {'product': 'Lednička', 'serial_number': '456213e', 'count': 5},
    {'product': 'Televize', 'serial_number': '5445', 'count': 7, 'diagonal': '35'},
    {'product': 'Počítač', 'serial_number': '745454', 'count': 13, 'CPU': 'AMD', 'RAM': '32 GB'}
]

response = customers_col.insert_many(customers)
print(f"Bylo přidání {response.inserted_ids} záznamů.")
response = storage_col.insert_many(products)
print(f"Bylo přidání {response.inserted_ids} záznamů.")
