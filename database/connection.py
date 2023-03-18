

from pprint import pprint
from fastapi import FastAPI
from pymongo import MongoClient



db = None
def connect_to_db(app: FastAPI):
    mongodb_client = MongoClient("mongodb://localhost:27017/")
    db = mongodb_client["To-do-list"]
    print('--connected to db--')

    print(db.list_collection_names())

    app.db = db
    print(app.db)
    collection = db['Item']
    print(collection)


    # users = db.get_collection('users')
    # entries = db.get_collection('Entries')

    # user = {
    #     "name": "hello"
    # }
    # # x = users.insert_one(user)

    # x = users.find()

    # for y in x:
    #     print("==", y)


    # print("--entries--\n\n", pprint(entries.find()), "--\n\n======")
    # print('----data---', pprint(x))

    return db