# # -*- coding: utf-8 -*-

# range
temp_list = range(5)
print(temp_list) # range(0, 5)
temp_list = list(temp_list)
print(temp_list) # [0, 1, 2, 3, 4]

# for list
users = [
    {'id': 100, 'name': 'sakura', 'age': 23},
    {'id': 101, 'name': 'oohara', 'age': 34},
    {'id': 102, 'name': 'kawa', 'age': 43},
]

# 推荐
for user in users:
    print(user)

# 很少用
for index in range(len(users)):
    print(index)
    print(users[index])

# 取所有name的值放入新列表
new_list = [user['name'] for user in users]
print(new_list)

# new_list = []
# for user in users:
#     new_list.append(user['name'])
# print(new_list)

# for dict
user_dict = {'id': 100, 'name': 'sakura', 'age': 23}
# for key in user_dict:
#     print('key={},val={}'.format(key, user_dict[key]))

# 推荐
for key,val in user_dict.items():
    print('key={},val={}'.format(key, val))

# for str
name = 'sakura'
for n in name:
    print(n)
