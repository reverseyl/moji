# -*- coding:utf8 -*-
# coding=utf-8
import time
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
while(True):
    fp = open('mojilog'+now, "a")  # 打开一个文本文件
    fp.write('start:'+now+'\n')  # 写入数据
    fp.close()  # 关闭文件