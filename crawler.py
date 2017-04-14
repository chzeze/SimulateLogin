import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#设置请求参数
values = {}
values['__VIEWSTATE'] = "/wEPDwUJODA3MTI1MjMyZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAgUIYnRuTG9naW4FDEltYWdlQnV0dG9uMQ=="
values['tbxUserID'] = "160320055"
values['InputPwd'] = "5026ZEze"
values['btnLogin.x'] = "55"
values['btnLogin.y'] = "23"
postdata = urllib.urlencode(values)

#登录教务系统的URL
loginUrl = 'http://yjsgl.fzu.edu.cn/login.aspx'
#模拟登录，并把cookie保存到变量
#设置header
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' 
opener.addheaders.append( ('Host', 'yjsgl.fzu.edu.cn') )
opener.addheaders.append( ('User-Agent', user_agent) )
opener.addheaders.append( ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8') )
opener.addheaders.append( ('Accept-Language', 'zh-CN,zh;q=0.8') ) 
opener.addheaders.append( ('Accept-Encoding', 'gzip, deflate') )
opener.addheaders.append( ('Connection', 'keep-alive') )
opener.addheaders.append( ('Referer', 'http://yjsgl.fzu.edu.cn/login.aspx') )

try:
    result = opener.open(loginUrl,postdata)
except opener.URLError, e:
    print e.reason

#==============================================================================
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value
#==============================================================================

#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://yjsgl.fzu.edu.cn/xsgl/xsxx_show.aspx'
#请求访问成绩查询网址
result = opener.open(gradeUrl)

html=result.read()
#print html

#开始解析
soup = BeautifulSoup(html)
#print type(soup.find_all("td", class_="tdright2"))
for tag in soup.find_all("td"):
    print tag.string




