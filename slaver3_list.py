# -*- coding: utf-8 -*-
import re
#from urllib.request import urlopen
#from urllib.request import Request
from common import httpSpider
from bs4 import BeautifulSoup
from lxml import etree
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.dianping
collection=db.shops	#店铺表

import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

ii=0

#id,店名,类别id
def insertShop(classid,shopList):
	for div in shopList:
		#print(div.get("href"))
		#print(div.get('title'))
		shopid = collection.insert({'shopname':div.get('title'),'classid':ObjectId(classid)})
		url = div.get("href")
		shopurl = '%s,%s,%s'%(classid,shopid,url)
		r.lpush('shopurl',shopurl)

def getCurPageList(classid,url):
	global ii
	ii += 1
	html = httpSpider(url)
	#print(html)
	
	selector = etree.HTML(html)

	divTits = selector.xpath('//div[@class="tit"]/a[@title]')
	insertShop(classid,divTits)
	'''
	for div in divTits:
		print(div.get("href"))
		print(div.get('title'))
	'''
	print('----------%i---------------'%(ii))
	#-----下一页--------------------------
	'''
	nextPage = selector.xpath('//a[@class="next"]/@href')
	if len(nextPage)>0:
		newUrl = nextPage[0]
		#print(nextPage[0])
		getCurPageList(newUrl)
	'''