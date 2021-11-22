from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    def f(a, b):
        if a > b:
            return 0
        if maximum_revenue_for_range[a][b] == 0:
            max_revenu_a = coins[a] + min(f(a + 1, b - 1), f(a + 2, b))
            max_revenu_b = coins[b] + min(f(a + 1, b - 1), f(a, b - 2))
            maximum_revenue_for_range[a][b] = max(max_revenu_a, max_revenu_b)
        return maximum_revenue_for_range[a][b]
    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return f(a=0, b=len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
