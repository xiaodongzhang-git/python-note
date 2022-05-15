# # -*- coding: utf-8 -*-

# 获取最小值
lower = lambda x,y: x if x<y else y
print(lower(2, -4))

# 根据key排序

d = [
    {'name': 'sakura', 'age': 18},
    {'name': 'kawa', 'age': 15},
    {'name': 'umi', 'age': 20},
]
d.sort(key=lambda x:x['age'])
print(d)