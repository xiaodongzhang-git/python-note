# # -*- coding: utf-8 -*-

ages = [18, 20, 30]

try:
    age = ages[3]
except IndexError as e:
    age = -1

print(age) # 假设是返回给前端的数据