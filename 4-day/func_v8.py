# # -*- coding: utf-8 -*-

# 接受函数为参数
from json.tool import main

def link_db(func):
    print('link db......')
    config_cloud = 1
    cloud = func(config_cloud)
    print(cloud)
    print('end....')

    def run_db(sql):
        return 20

    return run_db # 可返回函数

def get_cloud(flag):
    return 'ali' if flag == 0 else 'aws'

if __name__ == '__main__':
    func = link_db(get_cloud)
    print('-' * 100)
    count = func('select count(1) from student where id < 100')
    print(count)
