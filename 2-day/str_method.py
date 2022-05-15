# # -*- coding: utf-8 -*-

fruit = 'aPPle'
print(fruit.capitalize()) # Apple
print(fruit.count('P')) # 2

print('早安'.encode('UTF-8')) # b'\xe6\x97\xa9\xe5\xae\x89'
print(b'\xe6\x97\xa9\xe5\xae\x89'.decode('UTF-8')) #  早安

print(fruit.startswith('A')) # False
print(fruit.endswith('e')) # True

print(fruit.find('P')) # 1
print(fruit.find('f')) # -1
print(fruit.rfind('P')) # 2

print(fruit.isalpha()) # True
print(fruit.isdigit()) # False

print(fruit.lower()) # apple
print(fruit.upper()) # APPLE


print(','.join(['hello', 'word'])) # hello-word
print(fruit.replace('P', 'o')) # aoole

sentence = "   A man's best friends are his ten fingers.   "
print(sentence.split()) # ['A', "man's", 'best', 'friends', 'are', 'his', 'ten', 'fingers.']
print(sentence.strip()) # A man's best friends are his ten fingers.
