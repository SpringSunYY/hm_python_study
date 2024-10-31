import requests
import re

# 学校官网的URL
url = "https://www.gdust.edu.cn"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

try:
    # 发送GET请求获取官网页面内容
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html_content = response.text

    # 任务一：匹配 href 后的链接
    href_links = re.findall(r'href=["\'](.*?)["\']', html_content)
    print("任务一：匹配 href 后的链接")
    print(href_links)

    # 任务二：匹配“计算机学院”
    if '计算机学院' in html_content:
        print("\n任务二：找到“计算机学院”")
        print("计算机学院")

    # 任务三：匹配 <div> 标签的内容
    div_contents = re.findall(r'<div.*?>(.*?)</div>', html_content, re.S)
    print("\n任务三：<div> 标签的内容")
    print(div_contents)

except Exception as e:
    print("爬取失败:", e)
