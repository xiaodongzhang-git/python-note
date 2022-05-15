# # -*- coding: utf-8 -*-
class Person:
    name = '小新'

    def get_name(self):
        return self.name

person = Person()
print(person.get_name())
person.name = '阿呆'
print(person.get_name())