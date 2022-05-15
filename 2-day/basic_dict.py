# # -*- coding: utf-8 -*-


# 定义
d1 = {}
d2 = dict()

# add
d1['name'] = 'maru'
d1['age'] = 18
d1['is_boy'] = True
print(d1) # {'name': 'maru', 'age': 18, 'is_boy': True}

# query
name = d1['name']
print(name) # maru

# update
d1['age'] = 19
print(d1['age']) # 19

# del
del d1['name']
print(d1) # {'age': 19, 'is_boy': True}