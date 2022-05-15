# # -*- coding: utf-8 -*-

class AgeError(Exception):
    def __init__(self, message):
        print(message)

age = 20

try:
    if(age > 18):
        raise AgeError('age is error')
except AgeError as e:
    age = -1

print(age)