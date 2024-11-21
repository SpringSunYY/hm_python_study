import urllib.request
from lxml import etree

# 目标 URL
url = "https://careers.tencent.com/search.html"

# 自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# 获取网页内容
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html_content = response.read().decode("utf-8")

# 保存调试用 HTML 文件
with open("debug_tencent.html", "w", encoding="utf-8") as debug_file:
    debug_file.write(html_content)

# 使用 lxml 解析 HTML
tree = etree.HTML(html_content)

# 定位并提取职位信息
job_names = tree.xpath("//div[@class='recruit-title']/text()")
job_locations = tree.xpath("//p[@class='recruit-address']/text()")
job_dates = tree.xpath("//p[@class='recruit-time']/text()")

# 检查提取结果
if not job_names or not job_locations or not job_dates:
    print("未提取到职位信息，请检查 XPath 是否匹配或网页是否动态加载")
else:
    # 将职位信息保存到文本文档
    with open("tencent_jobs.txt", "w", encoding="utf-8") as file:
        for name, location, date in zip(job_names, job_locations, job_dates):
            file.write(f"职位名称: {name.strip()}, 地点: {location.strip()}, 发布时间: {date.strip()}\n")
    print("职位信息已保存到 tencent_jobs.txt")

import requests
import json

# 设置接口地址
url = "https://careers.tencent.com/tencentcareer/api/post/Query"

# 定义请求参数
params = {
    "timestamp": "1732156487823",  # 可动态生成时间戳
    "keyword": "",
    "pageIndex": 1,
    "pageSize": 10,  # 每页返回的数据量
    "language": "zh-cn",
    "area": "cn"
}

# 发送 GET 请求
response = requests.get(url, params=params)

# 解析返回的 JSON 数据
if response.status_code == 200:
    data = response.json()
    posts = data.get("Data", {}).get("Posts", [])
    if posts:
        # 保存职位信息到文件
        with open("tencent_jobs.txt", "w", encoding="utf-8") as file:
            for post in posts:
                file.write(f"职位名称: {post['RecruitPostName']}\n")
                file.write(f"地点: {post['LocationName']}\n")
                file.write(f"分类: {post['CategoryName']}\n")
                file.write(f"发布时间: {post['LastUpdateTime']}\n")
                file.write(f"详情链接: {post['PostURL']}\n")
                file.write("-" * 30 + "\n")
        print("职位信息已成功保存到 tencent_jobs.txt")
    else:
        print("未找到职位信息")
else:
    print("请求失败，状态码:", response.status_code)
