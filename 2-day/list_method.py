# # -*- coding: utf-8 -*-

arr = [1, 2, 3, 4]

# append
arr.append(5) # [1, 2, 3, 4, 5]
print(arr)

# copy
arr_copy = arr.copy()
print(arr_copy) # [1, 2, 3, 4, 5]

# clear
arr_copy.clear()
print(arr_copy) # []

# count
print(arr.count(1)) # 1
print(arr.count(6)) # 0

# extend
arr2 = ['a', 'b', 'c']
arr.extend(arr2)
print(arr) # [1, 2, 3, 4, 5, 'a', 'b', 'c']

# index
print(arr.index(3)) # 2
# print(arr.index(6)) # ValueError: 6 is not in list

# insert
arr.insert(0, 'new1')
print(arr) # ['new1', 1, 2, 3, 4, 5, 'a', 'b', 'c']

# pop
arr.pop() # デフォルトは最後の値です
print(arr) # ['new1', 1, 2, 3, 4, 5, 'a', 'b']
arr.pop(0)
print(arr) # [1, 2, 3, 4, 5, 'a', 'b']

# remove
arr.append('a')
print(arr) # [1, 2, 3, 4, 5, 'a', 'b', 'a']
arr.remove('a')
print(arr) # [1, 2, 3, 4, 5, 'b', 'a']

arr.reverse()
print(arr) # ['a', 'b', 5, 4, 3, 2, 1]

# arr.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
arr = [5, 4, 3, 2, 1]
arr.sort()
print(arr) # [1, 2, 3, 4, 5]

def isEven(e):
    return e%2 == 0

arr.sort(key=isEven)
print(arr) # [1, 3, 5, 2, 4]

