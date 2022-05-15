# # -*- coding: utf-8 -*-

# 参数可设默认值
def price_compute(price, kind=1):
    if kind == 1:
        return price * 1.1
    else:
        return price * 1.08

if __name__ == '__main__':
    not_necessity = 2
    price = 298
    total_price1 = price_compute(price)
    print(total_price1)
    total_price2 = price_compute(price, not_necessity)
    print(total_price2)