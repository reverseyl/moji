# -*- coding:utf8 -*-
# coding=utf-8
import json
import urllib2
import cookielib

filename = 'mojicookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 登录墨迹天气主页的URL
loginUrl = 'http://tianqi.moji.com/'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址，此网址是XMR网址
gradeUrl = 'http://tianqi.moji.com/index/getHour24'
# 请求访问查询网址
result = opener.open(gradeUrl)
page = result.read()
newpage = [json.loads(page)]
mojidict = newpage[0]['hour24'][0]
# 再次爬取PM2.5数据
gradeUrl = 'http://tianqi.moji.com/api/getAqi/undefined'
result = opener.open(gradeUrl)
page = result.read()
newpage = [json.loads(page)]
a = newpage[0]['hours'][24]
mojidict['aqi'] = a['aqi']
print mojidict
