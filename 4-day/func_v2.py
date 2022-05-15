# # -*- coding: utf-8 -*-

# 能传递参数
def price_compute(price, kind):
    if kind == 1:
        return price * 1.1 # return: 返回值，不继续往下走了
    else:
        return price * 1.08

if __name__ == '__main__':
    is_necessity = 1
    not_necessity = 2

    price = 298
    total_price = price_compute(price, not_necessity)
    # 通过参数名指定参数，位置可随意
    total_price = price_compute(kind=is_necessity, price=price)
    print(total_price)