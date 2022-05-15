# # -*- coding: utf-8 -*-
class Person:

    # 魔法方法
    def __init__(self,name, age, sex, phone):
        self._name = name
        self._age = age
        self._sex = sex
        self._phone = phone # _开头默认是私有的

    def get_info(self):
        return '姓名：{}\n年龄：{}\n性别：{}\n电话：{}'.format(self._name, self._age, self._sex, self._phone)

p1 = Person('小新', 5, '男', '110')
print(p1.get_info())
print('*' * 10)
p2 = Person('妮妮', 4, '女', '112')
print(p2.get_info())
