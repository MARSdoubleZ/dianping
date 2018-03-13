# -*- coding: utf-8 -*-
import urllib.request
from urllib.request import urlopen
from urllib.request import Request
import http.cookiejar

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

head = {  
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'  
}
def makeMyOpener(head):  
    cj = http.cookiejar.CookieJar()  
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
    header = []  
    for key, value in head.items():  
        elem = (key, value)
        header.append(elem)  
    opener.addheaders = header  
    return opener
def httpSpider(url):
	oper = makeMyOpener(head)
	req_timeout = 5
	uop = oper.open(url, timeout = req_timeout)
	data = uop.read()  
	html = data.decode()
	return html
'''
def httpSpider(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	req_timeout = 5
	cj = http.cookiejar.CookieJar()  

	req = Request(url=url,headers=headers)
	f = urlopen(req,None,req_timeout)
	s=f.read()
	html=s.decode("utf-8")
	return html
'''

def dynamicSpider(url):
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
		'Connection': 'keep-alive'
	}
	cap = DesiredCapabilities.PHANTOMJS.copy()	#使用copy()防止修改原代码定义dict
	for key, value in headers.items():
		cap['phantomjs.page.customHeaders.{}'.format(key)] = value
	cap["phantomjs.page.settings.loadImages"] = False
	driver = webdriver.PhantomJS(desired_capabilities=cap,executable_path='D:/Tools/python/spider/phantomjs-2.1.1-windows/bin/phantomjs.exe')
	driver.get(url)
	html = driver.page_source
	driver.quit()
	return html