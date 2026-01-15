# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class KongqizhiliangItem(scrapy.Item):
    # 城市
    cityname = scrapy.Field()
    # 站点
    positionname = scrapy.Field()
    # AQI
    aqi = scrapy.Field()
    # PM2_5
    pm25 = scrapy.Field()
    # PM10
    pm10 = scrapy.Field()
    # SO2
    so2 = scrapy.Field()
    # NO2
    no2 = scrapy.Field()
    # CO
    co = scrapy.Field()
    # O3
    o3 = scrapy.Field()

