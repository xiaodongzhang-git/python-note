# # -*- coding: utf-8 -*-

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 省略get和set

    # 被实例重写后就无法在该实例使用了
    def get_info(self):
        return '姓名：{}\n年龄：{}'.format(self._name, self._age)

class Student(Person):

    def __init__(self, name, age, stu_no, class_no):
        self._stu_no = stu_no
        self._class_no = class_no
        super().__init__(name, age)

    # get set 略

    # 重写（方法名和父类一样）
    def get_info(self):
        return '姓名：{}\n年龄：{}\n学生号：{}\n班级：{}'.format(self._name, self._age, self._stu_no, self._class_no)

class Teacher(Person):

    def __init__(self, name, age, job_no, money):
        self._job_no = job_no
        self._money = money
        super().__init__(name, age)

stu = Student('小新', 5, 'stu no 1', 'class no 1')
print(stu.get_info())
print('*' * 10)
tea = Teacher('小绿', 26, 'job no 1', 1000000)
print(tea.get_info())
