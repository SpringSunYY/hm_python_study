import requests
from lxml import html

# 百度搜索 URL，q 参数是搜索关键字
keyword = "传智播客"
url = f"https://www.baidu.com/s?wd={keyword}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# 获取网页源码
response = requests.get(url, headers=headers)
response.raise_for_status()  # 检查请求状态
html_content = response.text

# 打印网页内容
# print(html_content[:500])  # 打印前500个字符查看结构


# 使用 lxml 提取标题和链接
tree = html.fromstring(html_content)
titles = tree.xpath('//h3[contains(@class,"t")]/a/text()')  # 提取标题
links = tree.xpath('//h3[contains(@class,"t")]/a/@href')  # 提取链接

# 输出结果
for title, link in zip(titles, links):
    print(f"标题: {title}\n链接: {link}\n")
