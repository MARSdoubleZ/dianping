# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
from urllib.request import Request
from slaver3_list import getCurPageList
from bs4 import BeautifulSoup
from lxml import etree
'''
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db=client.dianping
collection=db.classification	#类别表
'''

import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

'''
1.从classurl中取得一个链接
2.根据此链接获得一个列表页面
3.分析获得页面上的店铺链接
4.获得下一页链接
5.继续爬取下一页信息,继续解析获得链接(重复2~5)
	直到没有下一页为止
'''
#1.从redis中获取一个链接
#classurls = bytes.decode(r.lindex('classurl',0))
list = r.lrange('classurl',0,-1)
for item in list:
	classurl = bytes.decode(item)		#二进制转字符串
	arr = classurl.split(',')
	print(arr[0])
	print(arr[1])
	#getCurPageList(arr[0],arr[1])
'''
print(classurls)
arr = classurls.split(',')

if int(arr[2])==16:
	#调用
	getCurPageList(arr[0],arr[1])
'''