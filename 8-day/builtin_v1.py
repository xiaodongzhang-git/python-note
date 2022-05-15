# # -*- coding: utf-8 -*-

import os
file_path = os.getcwd()
print(file_path) # 获取当前路径
all_file = os.listdir(file_path) # 获取路径下的所有文件名
for file_name in all_file:
    print(file_name)

# mkdir ：新建单个目录，若目录路径中父目录不存在，则创建失败
# makedirs ：新建多个目录，若目录路径中父目录不存在，则自动创建

# os.mkdir("test") # FileExistsError
os.rmdir("test")