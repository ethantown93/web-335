   # ============================================
# ; Title:  townsend-user-service.py
# ; Author: Professor Krasso
# ; Date:  26 June 2019
# ; Modified By: Ethan Townsend
# ; Description: CRUD operations
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

user={
    "first_name": "Ethan",
    "last_name": "Townsend",
    "email": "ethantown@gmail.com",
    "employee_id": "12345678",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(client)

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "12345678"}))