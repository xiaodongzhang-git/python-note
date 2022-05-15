# # -*- coding: utf-8 -*-

ages = [18, 20, 30, 40]
name = 'zhangsan'
try:
    age = ages[2]
    print(name + 1)
except Exception as e:
    print(e)
    age = -1

print(age) # 假设是返回给前端的数据