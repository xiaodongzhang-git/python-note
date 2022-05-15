# # -*- coding: utf-8 -*-
# int

# float to int
f_val1 = 3.999999999999
i_val1 = int(f_val1)
print(i_val1) # 3

# bool to int
b_val1 = True
b_val2 = False
i_val1 = int(b_val1)
i_val2 = int(b_val2)
print(i_val1) # 1
print(i_val2) # 0

# complex to int
# 不支持

# float

# int to float
i_val1 = 666
f_val1 = float(i_val1)
print(f_val1) # 666.0

# bool to float
b_val1 = True
b_val2 = False
f_val1 = float(b_val1)
f_val2 = float(b_val2)
print(f_val1) # 1.0
print(f_val2) # 0.0

# complex
# int to complex
i_val1 = 66
c_val1 = complex(i_val1)
print(c_val1) # (66+0j)

# float to complex
f_val1 = 1.3415
c_val2 = complex(f_val1)
print(c_val2) # (1.3415+0j)

# bool to complex
b_val1 = True
b_val2 = False
c_val1 = complex(b_val1)
c_val2 = complex(b_val2)
print(c_val1) # (1+0j)
print(c_val2) # 0j