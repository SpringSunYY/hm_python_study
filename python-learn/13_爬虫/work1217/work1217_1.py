import scrapy

from items import ItcItem


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["www.itcast.cn"]
    start_urls = ["https://www.itheima.com/teacher.html"]

    print('开始访问')

    def parse(self, response):
        print(f"Response Status: {response.status}")  # 输出响应的状态码
        if response.status == 200:
            print("访问成功")
        else:
            print(f"访问失败，状态码: {response.status}")
        print("访问成功")

        # 创建一个Item对象
        item = ItcItem.ItcItem()
        item['name'] = response.xpath('/html/head/title/text()').extract_first()
        print(item['name'])

        # 输出一些测试信息
        print(response.xpath('/html/body/div[1]/div[4]/div/div[1]/h2/text()').extract())
        print(response.css(
            '#mcsp 1 container > ul > li:nth-child(1) > div:nth-child(1) > div.main_mask > h2::text').extract())

        # 存放老师信息的集合
        items = []

        # 遍历所有符合条件的元素
        for each in response.xpath("//div[@class='li_txt']"):
            # 将数据封装到一个 Item 对象中
            item = ItcItem.ItcItem()
            # 使用 XPath 提取数据并处理
            name = each.xpath("h3/text()").extract_first()
            title = each.xpath("h4/text()").extract_first()
            info = each.xpath("p/text()").extract_first()

            # 将数据填充到 Item 对象中
            item["name"] = name
            item["zhicheng"] = title
            item["info"] = info

            # 添加到集合
            items.append(item)

        # 返回数据，不经过 pipeline
        return items
