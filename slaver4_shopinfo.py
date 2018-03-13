# -*- coding: utf-8 -*-
import re
#from urllib.request import urlopen
#from urllib.request import Request
from common import dynamicSpider
from bs4 import BeautifulSoup
from lxml import etree
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.dianping
collection=db.shops	#店铺表

import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

def getShopInfo(shopid,shopurl):
	html = dynamicSpider(shopurl)
	#print(html)
	selector = etree.HTML(html)
	divTits = selector.xpath('//p[@class="comment-all"]/a')
	print(divTits[0].get("href"))
	print(divTits[0].text)
	

list = r.lrange('shopurl',0,-1)
for item in list:
	classurl = bytes.decode(item)		#二进制转字符串
	arr = classurl.split(',')
	shopid = arr[1]
	shopurl = arr[2]
	print(shopid)
	print(shopurl)
	getShopInfo(shopid,shopurl)
	break