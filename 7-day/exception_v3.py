# # -*- coding: utf-8 -*-

ages = [18, 20, 30, 40]
name = 'zhangsan'
try:
    age = ages[3]
    print(name + 1)
except TypeError as e:
    age = -2
except IndexError as e:
    age = -1
else:
    print('ok')

print(age) # 假设是返回给前端的数据