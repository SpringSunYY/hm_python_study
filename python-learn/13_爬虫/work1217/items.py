import scrapy

class ItcItem(scrapy.Item):
    # 定义字段
    name = scrapy.Field()       # 名字
    zhicheng = scrapy.Field()   # 职称
    info = scrapy.Field()       # 简介
    bianhao = scrapy.Field()    # 编号
    status = scrapy.Field()     # 状态
    title = scrapy.Field()      # 标题
    time = scrapy.Field()       # 时间
    movie = scrapy.Field()      # 电影信息
