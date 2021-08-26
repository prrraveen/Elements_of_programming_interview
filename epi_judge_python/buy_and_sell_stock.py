from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(xs: List[float]) -> float:
    n = len(xs)
    result = 0
    min_so_far = float("inf")
    for i in range(n):
        if xs[i] < min_so_far:

            min_so_far = xs[i]
        diff = xs[i] - min_so_far
        if diff > result:
            result = diff
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
