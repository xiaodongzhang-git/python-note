# # -*- coding: utf-8 -*-

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 省略get和set

    def get_info(self):
        return '姓名：{}\n年龄：{}'.format(self._name, self._age)

class Student(Person):

    def __init__(self, name, age, stu_no, class_no):
        self._stu_no = stu_no
        self._class_no = class_no
        super().__init__(name, age)

    @property
    def stu_no(self):
        return self._stu_no

    # 其他 get set 略

stu = Student('小新', 5, 'stu no 1', 'class no 1')
print(stu.get_info())
print(stu.stu_no)