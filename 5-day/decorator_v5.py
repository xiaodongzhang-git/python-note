# # -*- coding: utf-8 -*-
import functools

def check_request(func):
    @functools.wraps(func)
    def wrapper(msg):
        check(msg)
        func(msg)
    return wrapper

def check(msg):
    for key,val in msg.items():
        if isinstance(val, int) and (val > 999 or val < 0):
            raise ValueError("整数范围错误")
        if isinstance(val, str):
            val.strip()
        if key == 'uid' and len(val) != 8:
            raise ValueError("uid格式错误")

@check_request
def get_user_info(request):
    # 查数据库
    pass

@check_request
def change_user_password(request):
    # 更改数据库
    pass

r1 = {'uid': 'jsdjfdsfss', 'age': -1, 'uname': 'zhangsan1212'}
get_user_info(r1)
r2 = {'uid': 'ksdfsadkf', 'age': 20, 'uname': 'lisi82838'}
change_user_password(r2)