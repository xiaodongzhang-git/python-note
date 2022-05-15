# # -*- coding: utf-8 -*-

class Person:

    def __init__(self, name, age, phone):
        self._name = name
        self._age = age
        self._phone = phone

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if len(phone) > 11:
            raise ValueError('phone error')
        self._phone = phone

    def get_info(self):
        return '姓名：{}\n年龄：{}\n电话：{}'.format(self._name, self._age, self._phone)

person = Person('小新', 5, '110')
person.phone = '12345678'
print(person.phone)
print(person.get_info())