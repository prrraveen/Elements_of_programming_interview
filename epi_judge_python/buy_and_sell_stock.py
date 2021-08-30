import math
from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(xs: List[float]) -> float:
    min_so_far = math.inf
    max_profit = 0
    for x in xs:
        min_so_far = min(min_so_far,  x)
        max_profit = max(max_profit, x - min_so_far)
    return max_profit




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
