# # -*- coding: utf-8 -*-
import re

# 只匹配开头
print(re.match('python', 'python is the best language. python is fine.'))
print(re.match('language', 'python is the best language. python is fine.'))

# 匹配全文，找到第一个就会停止往后找
print(re.search('python', 'python is the best language.'))
print(re.search('java', 'python is the best language.'))

# sub（正则，替换字符串，原字符串）
phone = "070-8485-5123# phone number"
print(phone)
num = re.sub(r'#.*$', "", phone)
print( "电话号码是: ", num  )


# 删除非数字(-)的字符串
# \d是任意数字，及[0-9]
# \D是任意非数字
num =  re.sub(r'\D', "", phone)
num =  re.sub(r'\D', "", phone)
print( "电话号码是 : ", num )

# re.compile()函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
# 供 match() 和 search() 这两个函数使用。
pattern = re.compile(r'[A-Z]+')
m = pattern.match('hello Python!')
print(m)

m = pattern.match('hello PYTHON. hello WORLD!', 6, 8)
print(m)
m = pattern.match('hello PYTHON. hello WORLD!', 6)
print(m)

pattern = re.compile(r'\d+')
m = pattern.findall('python 001 java 002 node 003')
print(m)


pattern = re.compile(r'\d+')
m = re.split('\d+', 'python001java002node003')
print(m)