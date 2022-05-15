# # -*- coding: utf-8 -*-
import  functools

# 参数固定的情况
def my_decorator(func):
    print('one')
    @functools.wraps(func)
    def wrapper(msg):
        print('one wrapper of decorator')
        func(msg)
    return wrapper

@my_decorator
def my_func(msg):
    print('hello {}'.format(msg))

my_func('python')