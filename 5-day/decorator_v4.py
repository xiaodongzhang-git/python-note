# # -*- coding: utf-8 -*-
import functools

def login_check(func):
    @functools.wraps(func)
    def wrapper(msg):
        token = msg.get('token')
        if not token:
            raise ValueError('token不存在')

        #请求第三方接口判断token是否有效，这里用if判断长度代替
        if not len(token) == 8:
            raise ValueError('token无效')

        func(msg)
    return wrapper

@login_check
def get_user_info(request):
    # 查数据库
    return {'uid': 'jsdjfdsfss', 'name': 'zhangsan', 'age': 5}

r1 = {'uid': 'jsdjfdsfss', 'token': 'kjskdfsakdfksadfasdkfadsfk'}
res = get_user_info(r1)
print(res)
