# # -*- coding: utf-8 -*-

# break
users = [
    {'id': 100, 'name': 'sakura', 'age': 11},
    {'id': 101, 'name': 'oohara', 'age': 22},
    {'id': 102, 'name': 'kawa', 'age': 33},
    {'id': 103, 'name': 'sora', 'age': 44},
    {'id': 104, 'name': 'umi', 'age': 27},
]
target_name = 'kawa'
target_dic = {}
for user in users:
    if user['name'] > target_name:
        target_dic = user
        break
print(target_dic)

# continue
# 不超过30岁的放入一个新列表
target_list = []
for user in users:
    if user['age'] > 30:
        continue
    target_list.append(user)
print(target_list)