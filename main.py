# coding=utf-8
# 墨迹天气气候存数据库程序
# 最后编辑时间：2016年10月20日16:51:19
import json
import urllib2
import cookielib
import MySQLdb
import time

#天气提取
def mojitiqu():
    filename = 'mojicookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    #登录墨迹天气主页的URL
    loginUrl = 'http://tianqi.moji.com/'
    #模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl)
    #保存cookie到cookie.txt中
    cookie.save(ignore_discard=True, ignore_expires=True)
    #利用cookie请求访问另一个网址，此网址是XMR网址
    gradeUrl = 'http://tianqi.moji.com/index/getHour24'
    #请求访问查询网址
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
    return mojidict

# 打开数据库连接
db= MySQLdb.Connect(port=3306, user="root", passwd="3119966", db="samp_db",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
#'''
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS MOJI2")

# 创建数据表SQL语句
sql = """CREATE TABLE MOJI2 (
        hour INT,
        date CHAR(255),
        conditions CHAR(255),
        wspd CHAR(255),
        temp INT,
        windlevel INT,
        wdir CHAR(255),
        humidity INT,
        aqi INT)"""
cursor.execute(sql)
db.commit()
#'''
#设置所需数据
tianqi_list = {}
#新建日志
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
filename = 'mojilog'+now
fp = open(filename, "w+b")  # 打开一个文本文件
fp.write('start:'+now+'\r\n')  # 写入数据
fp.close()  # 关闭文件
'''
while(True):
    tianqi_list = mojitiqu()
    print tianqi_list['Fpredict_hour']

    sql = "INSERT INTO MOJI(hour,date,conditions,wspd,temp,windlevel,wdir,humidity,aqi)" \
          "VALUES('%d','%s','%s','%s','%d','%d','%s','%d','%d')" \
          % (
              tianqi_list['Fpredict_hour'], tianqi_list['Fpredict_date'], tianqi_list['Fcondition'], tianqi_list['Fwspd'], tianqi_list['Ftemp'], tianqi_list['wind_level'],
              tianqi_list['Fwdir'], tianqi_list['Fhumidity'], tianqi_list['aqi']
          )
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    #延时函数
    time.sleep(3600)
 '''
while True:
    fails = 0
    while True:
        try:
            if fails >= 10:
                #print("fail 5 times" )
                fp = open(filename, "a")  # 打开一个文本文件
                fp.write('error:'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'\n')  # 写入数据
                fp.close()  # 关闭文件
                break
            tianqi_list = mojitiqu()
            print tianqi_list['Fpredict_hour']
            sql = "INSERT INTO MOJI2(hour,date,conditions,wspd,temp,windlevel,wdir,humidity,aqi)" \
                  "VALUES('%d','%s','%s','%s','%d','%d','%s','%d','%d')" \
                  % (
                      tianqi_list['Fpredict_hour'], tianqi_list['Fpredict_date'], tianqi_list['Fcondition'],
                      tianqi_list['Fwspd'], tianqi_list['Ftemp'], tianqi_list['wind_level'],
                      tianqi_list['Fwdir'], tianqi_list['Fhumidity'], tianqi_list['aqi']
                  )
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            fp = open(filename, "a")  # 打开一个文本文件
            fp.write('record:' + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '\n')  # 写入数据
            fp.close()  # 关闭文件
        except:
            fails += 1
            print '失败%d次'%fails
            # 延时函数
            time.sleep(60)
        else:
            break
    #延时函数
    time.sleep(3600)