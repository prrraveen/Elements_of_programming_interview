from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    max_profit_each_day = [0] * len(prices)
    min_stock_price_till_now = float('inf')

    for i, stock_price in enumerate(prices):
        min_stock_price_till_now = min(min_stock_price_till_now, stock_price)
        max_profit_each_day[i] = stock_price - min_stock_price_till_now

    print(F"max_profit_each_day = {max_profit_each_day}")



xs = [12, 11, 13, 9, 12, 8, 14, 13, 15]
xs = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(F"buy_and_sell_stock_twice(xs) = {buy_and_sell_stock_twice(xs)}")



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
