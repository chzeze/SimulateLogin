# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:12:55 2017

@author: zeze
"""

import cookielib
import urllib2
 
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
Url = urllib2.Request("http://yjsgl.fzu.edu.cn/xsgl/xsxx_show.aspx")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(Url)
print response.read()