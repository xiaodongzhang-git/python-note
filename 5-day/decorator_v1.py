# # -*- coding: utf-8 -*-
import  functools

def one_decorator(func):
    print('one')
    @functools.wraps(func)
    def wrapper():
        print('one wrapper of decorator')
        func()
    return wrapper

def two_decorator(func):
    print('two')
    @functools.wraps(func)
    def wrapper():
        print('two wrapper of decorator')
        func()
    return wrapper

# 多个的情况，执行顺序是由里到外
@two_decorator
@one_decorator
def my_func():
    print('hello python')

my_func()