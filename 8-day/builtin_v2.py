# # -*- coding: utf-8 -*-
import re

phone_re = '^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\\d{8}$'
if not re.match(phone_re, '15363748194'):
    print('phone is error')

res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
for r in res:
    print(r)
