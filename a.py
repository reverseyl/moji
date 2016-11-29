# -*- coding:utf8 -*-
# coding=utf-8
#最后编辑时间：2016年10月13日20:57:05
import json
import urllib2
import cookielib
import MySQLdb
"""CREATE TABLE TEST2 (
        num CHAR(255),
        title TEXT,
        publisher CHAR(255),
        authors TEXT,
        authorinstitution TEXT,
        date  CHAR(255),
        issn CHAR(255),
        isbn CHAR(255),
        doi CHAR(255),
        keywords TEXT)"""
# 打开数据库连接
db= MySQLdb.Connect(port=3306, user="root", passwd="3119966", db="samp_db")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS MOJI")

# 创建数据表SQL语句
sql = """CREATE TABLE MOJI (
        hour INT,
        date CHAR(255),
        conditions CHAR(255),
        wspd CHAR(255),
        temp INT,
        windlevel INT,
        wdir CHAR(255),
        humidity INT)"""
cursor.execute(sql)
db.commit()