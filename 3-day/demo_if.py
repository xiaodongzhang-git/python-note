# # -*- coding: utf-8 -*-

score = 70
if score > 60:
    print('合格')
else:
    print('不合格')
#output: 合格

a = []
b = {}
c = 0
d = ''
# 上面四个都是 False
if a:
    print('true')
else:
    print('false')

# not false --> true  true --> false
if not a:
    print('false')
else:
    print('true')

print('-' * 100)

# and  or
a = True
b = False
if a and b:
    print('botn is true')

if a or b:
    print('At least one is true')

age = input('几岁?\n') # type is str
if int(age)>18:
    print('能喝酒')
else:
    print('不能喝酒')