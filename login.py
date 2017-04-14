# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:12:55 2017

@author: zeze
"""

import cookielib
import urllib2
from bs4 import BeautifulSoup
 
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
Url = urllib2.Request("http://yjsgl.fzu.edu.cn/xsgl/xsxx_show.aspx")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' 
opener.addheaders.append( ('Host', 'yjsgl.fzu.edu.cn') )
opener.addheaders.append( ('User-Agent', user_agent) )
opener.addheaders.append( ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8') )
opener.addheaders.append( ('Accept-Language', 'zh-CN,zh;q=0.8') ) 
opener.addheaders.append( ('Accept-Encoding', 'gzip, deflate') )
opener.addheaders.append( ('Connection', 'keep-alive') )
opener.addheaders.append( ('Referer', 'http://yjsgl.fzu.edu.cn/login.aspx') )

response = opener.open(Url)
html=response.read()
#开始解析
soup = BeautifulSoup(html)
#print type(soup.find_all("td", class_="tdright2"))
for tag in soup.find_all("td"):
    print tag.string