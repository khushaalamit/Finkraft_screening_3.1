import csv

import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient(
    "mongodb+srv://corecode:leverage1@cluster0.2gffoqa.mongodb.net/?retryWrites=true&w=majority")
db = client.test


db_names = client.list_database_names()
if "airlines" in db_names:
    print("DB is present")


database = client["airlines"]

collection = database["akasa_input"]
with open("Akasa_PNR_Consolidated.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    collection.insert_many(data)
