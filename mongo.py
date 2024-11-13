from pymongo import MongoClient
from datetime import * 
client = MongoClient('mongodb://localhost:27017/')

db = client['PYTT']  # replace 'mydatabase' with your database name
collection = db['PYT']  # replace 'mycollection' with your collection name
def insert(dat):

    collection.insert_one(dat)


def extract(datt):
    filtered_data = collection.find(datt)  # Use datt directly
    ls = []
    for document in filtered_data:
        ls.append(document)
    return ls


def dell(dat):   
     result = collection.delete_one(dat)
     print(f"Deleted {result.deleted_count} document(s)")




