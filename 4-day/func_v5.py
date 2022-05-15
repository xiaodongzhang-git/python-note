# # -*- coding: utf-8 -*-

# 参数是不变对象情况
def change_age(age):
    age += 1
    print(id(age)) # 4484848864

# 参数是可变对象情况
def change_list(nums):
    nums.append('test')

if __name__ == '__main__':
    age = 18
    print(id(age)) # 4484848832
    change_age(age)
    print(id(age)) # 4484848832

    nums = [1, 2, 3, 4]
    print(nums) # [1, 2, 3, 4]
    change_list(nums)
    print(nums) # [1, 2, 3, 4, 'test']