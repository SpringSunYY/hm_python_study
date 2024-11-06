import requests
import re
from lxml import html

# 学校官网的URL
url = "https://www.gdust.edu.cn"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

try:
    # 发送GET请求获取官网页面内容
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    html_content = response.text

    # 任务一：通过正则表达式匹配“计算机学院”
    match = re.search(r'计算机学院', html_content)
    if match:
        print("任务一：通过正则表达式获取“计算机学院”")
        print(match.group())
    else:
        print("任务一：未找到“计算机学院”")

    # 任务二：通过XPath匹配“计算机学院”
    tree = html.fromstring(response.text)
    result = tree.xpath("//*[contains(text(), '计算机学院')]")
    if result:
        print("\n任务二：通过XPath获取“计算机学院”")
        print(result[0].text_content())  # 获取该元素的文本内容
    else:
        print("\n任务二：未找到“计算机学院”")

except Exception as e:
    print("爬取失败:", e)
