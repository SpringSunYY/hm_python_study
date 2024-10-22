import requests

# kv = {'wd': 'Python'}
# kx = {'user-agent': 'Mozilla/5.0'}
# url = "http://www.baidu.com/s"
# try:
#     r = requests.get(url, params=kv, headers=kx)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[0:1000])
# except:
#     print("爬取失败")
#
# import requests
# path = "abc.png"
# url = "https://portal.gdust.edu.cn/images/gk-logo.png"
# r = requests.get(url)
# requests.status_codes
# with open(path, "wb") as f:
#     f.write(r.content)
# f.close()


import requests
# 搜索关键词参数
kv = {'q': 'Python'}  # 关键词为“Python”
# 请求头
kx = {'user-agent': 'Mozilla/5.0'}
# 360搜索的URL
url = "https://www.so.com/s"
try:
    r = requests.get(url, params=kv, headers=kx)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:10000])
except Exception as e:
    print("爬取失败:", e)

import requests
# 搜索关键词参数
kv = {
    'title': 'a',
    'modelid': 49,
    'siteid': 1
}

# 请求头
kx = {'user-agent': 'Mozilla/5.0'}
# 目标URL
url = "https://www.gdust.edu.cn/e/search/"
try:
    r = requests.get(url, params=kv, headers=kx)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:10000])
except Exception as e:
    print("爬取失败:", e)
