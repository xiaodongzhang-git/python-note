# # -*- coding: utf-8 -*-

# bool-> int-> float-> complex

i_val = 10
f_val = 1.314
c_val = 5 + 2j
b_val = True

# int + bool
res1 = i_val + b_val
print('res={} type is {}'.format(res1, type(res1))) # res=11 type is <type 'int'>

# int + float
res2 = i_val + f_val
print('res={} type is {}'.format(res2, type(res2))) # res=11.314 type is <type 'float'>

# int + complex
res3 = i_val + c_val
print('res={} type is {}'.format(res3, type(res3))) # res=(15+2j) type is <type 'complex'>

# float + bool
res4 = f_val + b_val
print('res={} type is {}'.format(res4, type(res4))) # res=2.314 type is <type 'float'>

# float + complex
res5 = f_val + c_val
print('res={} type is {}'.format(res5, type(res5))) # res=(6.314+2j) type is <type 'complex'>

# bool + complex
res6 = b_val + c_val
print('res={} type is {}'.format(res6, type(res6))) # res=(6+2j) type is <type 'complex'>
