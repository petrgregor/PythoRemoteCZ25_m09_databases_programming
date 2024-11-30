from connect_mongo import db_pr25

#customers_collection = db_pr25["customers"]
customers_collection = db_pr25.create_collection(
    "customers",
    collation={
        "locale": "cs",  # Nastavení české lokalizace
        "strength": 1    # Ignoruje rozdíly mezi velkými a malými písmeny
    }
)

customers = [
    {"name": "Adam", "surname": "Novák", "address": "Hlavní 25, Brno"},
    {"name": "Bedřich", "surname": "Svoboda", "address": "Jarní 1, Praha"},
    {"name": "Ctibor", "surname": "Novotný", "address": "Letní 21, Olomouc"},

    {"_id": 1, "name": "Dan", "surname": "Lejska", "address": "Podzimní 13, Ostrava"},
    {"_id": 2, "name": "Evžen", "surname": "Brzobohatý", "address": "Zimní 112, Jihlava"},
    {"_id": 3, "name": "Filip", "surname": "Rychlechudý", "address": "Zelená 15a, Hradec Králové"},
    {"_id": 4, "name": "Gustav", "surname": "Novák", "address": "Modrá 2, Písek"},
    {"_id": 5, "name": "Helena", "surname": "Daniel", "address": "Červená 13, Praha"},

    {"_id": 6, "name": "Ivan"},
    {"_id": 7, "name": "Jan", "surname": "Bledý", "email": "jan@bledy.cz"},
    {"_id": 5, "name": "Karel", "surname": "Trojan", "phone_number": "+420777123456"}
]

response = customers_collection.insert_many(customers)

print(f"Last inserted ids: {response.inserted_ids}")
