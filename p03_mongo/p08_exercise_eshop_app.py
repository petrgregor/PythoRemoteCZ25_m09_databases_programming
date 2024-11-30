from pymongo.errors import OperationFailure

from connect_mongo import db_pr25, mongo_client

customers_col = db_pr25['customers']
storage_col = db_pr25['storage']
order_col = db_pr25['order']

# Aleš Hodný si koupí ledničku
product = storage_col.find_one({'product': 'Lednička'})
count = 1
if int(product['count']) >= count:
    print(f"Lednička je na skladě: {product}")

    customer = customers_col.find_one({'name': 'Aleš', 'surname': 'Hodný'})
    print(customer)

    try:
        with mongo_client.start_session() as session:
            with session.start_transaction():
                order_col.insert_one({'customer': customer, 'product': product, 'count': count})
                storage_col.update_one({'product': 'Lednička'}, {'$set': {'count': int(product['count'])-count}})
                #customers_col.update_one({'name': 'Aleš', 'surname': 'Hodný'},
                #                         {'$set': {'order': {'product': product, 'count': count}}})
    except OperationFailure as e:
        print(f"ERROR: {e}")

    for response in order_col.find():
        print(response)
else:
    print("Na skladě není dostatečný počet kusů.")


