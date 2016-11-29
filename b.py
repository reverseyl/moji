# -*- coding:utf8 -*-
# coding=utf-8
import cookielib
import urllib2
import json

dict1 = dict(a =1,b =2,c=3,d=4,e=5,f=6)
print dict1
dict2 = sorted(dict1.iteritems(),key = lambda x:x[1],reverse=True)
keyss = lambda x:x[0]
dict3 = [keyss(items) for items in dict2]
print dict3