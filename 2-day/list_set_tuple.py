# # -*- coding: utf-8 -*-

# list
list_1 = [1, 1, 2, 4, 6, 8]
print(list_1) # [1, 1, 2, 4, 6, 8]
list_1[2] = 3
print(list_1) # [1, 1, 3, 4, 6, 8]

# tuple
tuple_1 = (1, 1, 2, 4, 6, 8)
print(tuple_1) # (1, 1, 2, 4, 6, 8)
# tuple_1[2] = 3 # TypeError: 'tuple' object does not support item assignment

# set
list_2 = [3, 3, 3, 3, 3, 4]
# set_1 = set(list_2)
# print(set_1) # {3, 4}
list_2 = list(set(list_2))
print(list_2)