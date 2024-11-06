import pymongo as mongodb

# 连接到 MongoDB 数据库
client = mongodb.MongoClient("mongodb://admin:yy0908..@localhost:27017")
print(client)
# 切换到 yy 数据库
db = client.yy
collection = db.mycol1
print(collection)
# (1) 插入一条记录
collection.insert_one({"name": "abcd", "age": 18, "grade": 98})

# (2) 插入两条记录
collection.insert_many([
    {"name": "aaaa", "age": 19, "grade": 94},
    {"name": "bbbb", "age": 20, "grade": 98}
])

# (3) 查询集合中的所有文档
all_documents = collection.find()
for doc in all_documents:
    print(doc)

# (4) 删除 name 为 "abcd" 的文档
collection.delete_one({"name": "abcd"})

# (5) 更新 name 为 "aaaa" 的文档，更新为 name 为 "bbbb"
collection.update_one({"name": "aaaa"}, {"$set": {"name": "bbbb"}})

# (6) 将 name 为 "bbbb" 的所有文档更新为 name 为 "cccc"
collection.update_many({"name": "bbbb"}, {"$set": {"name": "cccc"}})

# (7) 统计目前集合中有多少条文档记录
count = collection.count_documents({})
print(f"当前集合中有 {count} 条文档记录。")
