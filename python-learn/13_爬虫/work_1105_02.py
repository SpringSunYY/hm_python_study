import requests
from lxml import html

# 任务1：爬取菜单项
url_menu = "http://www.aolingdata.com"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

try:
    # 获取主页内容
    response_menu = requests.get(url_menu, headers=headers)
    response_menu.raise_for_status()
    tree_menu = html.fromstring(response_menu.text)

    # 解析菜单项
    menu_items = tree_menu.xpath("//span[contains(@class, 'J_nav_item_name')]/text()")
    print("任务1：官网菜单项")
    for item in menu_items:
        print(item.strip())

except Exception as e:
    print("任务1 爬取失败:", e)

# 任务2：爬取图标和文字
url_content = "http://www.aolingdata.com/col.jsp?id=105"

try:
    # 获取内容页内容
    response = requests.get(url_content, headers=headers)
    response.raise_for_status()
    tree = html.fromstring(response.text)

    # 提取图标和文字内容
    images = tree.xpath("//a[@class='J_floatImg_jump f_floatImg_jump floatImgALink']//img/@data-original")
    texts = tree.xpath("//a[@target='_blank']/font[@color='#333333']/text()")

    # 输出结果
    print("图标和对应文字内容：")
    # 输出结果
    for link, text in zip(images, texts):
        print(f"链接: {link}, 文字: {text.strip()}")

except Exception as e:
    print("任务2 爬取失败:", e)
