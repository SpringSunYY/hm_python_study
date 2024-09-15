"""
演示JSON数据和Python字典的相互转换
"""
import json
# JSON数据
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
print(data)
print("--------------------------------------")
# 将列表转换为JSON
json_data = json.dumps(data, ensure_ascii=False)
print(type(json_data))
print(json_data)
print("--------------------------------------")

# 将JSON转换为Python数据
data = json.loads(json_data)
print(type(data))
print(data)
print("--------------------------------------")

