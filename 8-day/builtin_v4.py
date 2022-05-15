# # -*- coding: utf-8 -*-
from datetime import date
import time
now = date.today()
print(now)

now_time = time.time() # 时间戳
print(now_time)


localtime = time.localtime(time.time()) # 获取本地时间
print(localtime)
f_localtime = time.asctime( time.localtime(time.time()) ) # 获取格式化的时间
print(f_localtime)
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
