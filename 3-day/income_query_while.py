# # -*- coding: utf-8 -*-

print('東京的平均年收入调查。\n')

is_continue = True

while is_continue:
    print('start-------------------')

    income = int(input('输入年龄\n'))

    if 19<income<30:
        print('20代的平均年收是348万元。')
    elif 29<income<40:
        print('30代的平均年收是444万元。')
    elif 39<income<50:
        print('40代的平均年收是510万元。')
    elif 49<income<60:
        print('50代的平均年收是613万元。')
    else:
        print('年龄输入错误，请重新输入。')
    print('end-------------------')