import urllib.request

from urllib3 import request

# response = urllib.request.urlopen('http://python.org')
#
# print(response.geturl())
# print(response.getcode())
# print(response.info())
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
#
# request = urllib.request.Request('http://www.baidu.com')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


import urllib.request

#  爬取百度官网源码
def fetch_with_urlopen(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

# 爬取广东科技学院官网源码
def fetch_with_request(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

# 爬取百度官网
baidu_url = 'https://www.baidu.com'
baidu_html = fetch_with_urlopen(baidu_url)


# 爬取广东科技学院官网
gdstcc_url = 'https://portal.gdust.edu.cn'
gdstcc_html = fetch_with_request(gdstcc_url)


# 显示部分内容
print("百度官网源码前500个字符：")
print(baidu_html[:500])

print("\n广东科技学院官网源码前500个字符：")
print(gdstcc_html[:500])


import urllib.parse

###
# 设置 data 参数
data = {
    '主页': 'https://www.baidu.com',
    'name': '广东科技学院'
}

# 使用 urlencode 方法进行编码
encoded_data = urllib.parse.urlencode(data)
print("使用 urlencode 编码后的结果：")
print(encoded_data)

# 使用 unquote 方法解码
decoded_data = urllib.parse.unquote(encoded_data)
print("\n使用 unquote 解码后的结果：")
print(decoded_data)

# 使用 quote 方法对原始字符串编码
original_string = 'https://www.baidu.com?name=广东科技学院'
quoted_string = urllib.parse.quote(original_string)
print("\n使用 quote 编码后的结果：")
print(quoted_string)
###