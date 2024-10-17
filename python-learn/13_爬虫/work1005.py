import requests

# # 构建请求的URL和参数
# base_url = "https://www.gdust.edu.cn/e/search/"
# params = {
#     "title": "国庆",   # 搜索关键词
#     "modelid": 49,
#     "siteid": 1
# }
#
# # 发送GET请求
# response = requests.get(base_url, params=params)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 输出响应的HTML源代码
#     html_content = response.text
#     print("获取到的页面源代码:")
#     print(html_content)
# else:
#     print(f"请求失败，状态码: {response.status_code}")


import requests

# 目标URL和搜索参数
base_url = "http://www.tipdm.com/search.jspx"  # 假设搜索接口是这个
params = {
    "q": "爬虫"  # 搜索关键词
}

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# 发送GET请求
response = requests.get(base_url, params=params,headers=headers)

# 获取响应的URL
print("获取响应的URL:")
print(response.url)

# 获取响应码
print("\n获取响应码:")
print(response.status_code)

# 获取页面的元信息
print("\n获取页面的元信息:")
print(response.headers)

# 输出页面的源代码
if response.status_code == 200:
    print("\n获取到的页面源代码:")
    print(response.text)
else:
    print(f"请求失败，状态码: {response.status_code}")
