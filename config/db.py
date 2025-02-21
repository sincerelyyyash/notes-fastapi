from pymongo import MongoClient
MONGO_URI = "mongodb://admin:myPassword@localhost:27017"

conn = MongoClient(MONGO_URI)
