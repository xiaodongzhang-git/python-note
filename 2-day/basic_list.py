# # -*- coding: utf-8 -*-


# list定义 index---->0は开头、-1は结尾
arr = [1, 2, 'str', ['a', 'b'], {'name': 'sakura'}]

# add
arr.append(True)
print(arr) # [1, 2, 'str', ['a', 'b'], {'name': 'sakura'}, True]

# query
print(arr[0]) # 1

# update
arr[2] = 'new str'
print(arr) # [1, 2, 'new str', ['a', 'b'], {'name': 'sakura'}, True]

# del
del arr[0]
print(arr) # [2, 'new str', ['a', 'b'], {'name': 'sakura'}, True]
del arr[-1]
print(arr) # [2, 'new str', ['a', 'b'], {'name': 'sakura'}]
