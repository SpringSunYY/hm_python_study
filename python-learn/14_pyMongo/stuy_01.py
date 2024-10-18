import pymongo as mongodb

print(mongodb)
print(mongodb.__version__)

# mongodb.MongoClient('mongodb://192.168.10.100:27017')
# client= mongodb.MongoClient(host='192.168.10.100', port=27017)
client = mongodb.MongoClient("mongodb://admin:admin123@192.168.10.100:27017")
client_db = client.myTest  # client_db = client['myTest']
# mongodb_collection= client_db['myTestCollection']
mongodb_collection = client_db.myTestCollection
print(mongodb_collection)
print(client_db)
print(client)
print("--------------------------------------")

res = mongodb_collection.find({
    "name": "YY"
})
print(type(res))
