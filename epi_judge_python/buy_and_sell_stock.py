import math

from test_framework import generic_test

# def buy_and_sell_stock_once(xs: List[float]) -> float:
#     max_profit_so_far = 0
#     for i in range(len(xs)):
#         for j in range(i+1, len(xs)):
#             max_profit_so_far = max(max_profit_so_far, xs[j] - xs[i])
#     return max_profit_so_far

from typing import List
def buy_and_sell_stock_once(xs: List[float]) -> float:
    min_so_far = float('inf')
    max_profit_so_far = 0
    for x in xs:
        min_so_far = min(min_so_far, x)
        max_profit_so_far = max(max_profit_so_far, x - min_so_far)
    return max_profit_so_far

# xs = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# print(F"buy_and_sell_stock_once(xs) = {buy_and_sell_stock_once(xs)}")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
