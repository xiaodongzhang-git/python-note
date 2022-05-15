# # -*- coding: utf-8 -*-

func_a = lambda : print('hello word')
# 上面的匿名函数等同于下面
# def func_a():
#     print('hello word')
print(func_a())

func_add1 = lambda x, y: x + y
# def func_add1(x, y):
#     return x + y
print(func_add1(10, 20))

func_add2 = lambda x, y=20: x + y
# def func_add2(x, y=20):
#     return x + y
print(func_add2(10))