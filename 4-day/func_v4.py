# # -*- coding: utf-8 -*-

# 参数个数可不固定
def test_arg(*args):
    print(args)
    for arg in args:
        print(arg)

def test_kwargs(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print('{}: {}'.format(k, v))

def test(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    a = 1
    b = 'test'
    c = [1,2]
    d = {'name': 'sakura'}
    test_arg(a, b, c, d)
    test_kwargs(name=a, age=b, sex=c, addrees=d)
    
    test(1, 2, 3, name='sakura', age=20)