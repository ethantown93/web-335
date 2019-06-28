   # ============================================
# ; Title:  townsend-user-update.py
# ; Author: Professor Krasso
# ; Date:  27 June 2019
# ; Modified By: Ethan Townsend
# ; Description: CRUD operations
# ;===========================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.user.update_one(
    {"employee_id": 12345678},
    {
        "$set": {
            "email": "newuseremail@this.com"
        }
    }
    
)

pprint.pprint(db.user.fine_one({"employee_id": 12345678}))