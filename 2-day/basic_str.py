# # -*- coding: utf-8 -*-

str1 = 'apple' # 一般的に
str2 = "orange" # 不変の変数が定義されている場合に
str3 = '''banana''' # 注釈の場合に

# 異なる引用符は相互にネストできます。
str4 = "My favorite fruit is ‘strawberry’"
print(str4) # My favorite fruit is ‘strawberry’

str5 = '''Do 'you' like to eat "apples"?'''
print(str5) # Do 'you' like to eat "apples"?

# indexを介して要素を表示する
sentence = "A man's best friends are his ten fingers."
print(sentence[0]) # A  0は常にコードの最初の位置
print(sentence[-1]) # . -1は最後の位置
sentence1 = sentence[: 12]
print(sentence1) # A man's best
sentence2 = sentence[12: -1]
print(sentence2) #  friends are his ten fingers
# 逆順
sentence3 = sentence[12: 7: -1]
print(sentence3) # tseb