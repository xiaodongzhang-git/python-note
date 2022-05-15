# # -*- coding: utf-8 -*-
import  functools

# 参数不固定的情况
def my_decorator(func):
    print('my_decorator')
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('wrapper of my_decorator')
        func(*args,**kwargs)
    return wrapper

@my_decorator
def one_func(a, b):
    print(a + b)

@my_decorator
def two_func(a, b, c):
    print(a + b + c)

one_func(1, 2)
two_func(1, 2, 3)

