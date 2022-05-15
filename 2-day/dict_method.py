# # -*- coding: utf-8 -*-

d1 = {'name': 'asa', 'age': 8}

# copy
d2 = d1.copy()
print(d2) # {'name': 'asa', 'age': 8}

# get
name = d1.get('name')
print(name) # asa

is_boy = d1.get('is_body')
print(is_boy) # None
is_boy = d1.get('is_body', False)
print(is_boy) # False

# items
items = d1.items()
print(items) # dict_items([('name', 'asa'), ('age', 8)])

# keys
keys = d1.keys()
print(keys) # dict_keys(['name', 'age'])

# values
values = d1.values()
print(values) # dict_values(['asa', 8])

# pop
pop_val = d1.pop('name') # asa
print(pop_val)
print(d1) # {'age': 8}

# popitem
pop_item = d1.popitem()
print(pop_item) # ('age', 8)
print(d1) # {}


# update
d3 = {'name': 'asa', 'age': 8}
d4 = {'name': 'sakura', 'is_body': False}
d3.update(d4)
print(d3) # {'name': 'sakura', 'age': 8, 'is_body': False}

# clear
d3.clear()
print(d3) # {}