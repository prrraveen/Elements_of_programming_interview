import bisect
import collections
from typing import List

from test_framework import generic_test


# def smallest_nonconstructible_value(A: List[int]) -> int:
#     A.sort()
#     for i in range(1, sum(A)+2):
#         coins = collections.Counter(A)
#         change = i
#         while change != 0:
#             print(F"change = {change}")
#             smaller_coin_idx = bisect.bisect_left(A, change)
#             change -= A[smaller_coin_idx]
#         # print(F"i = {i}")
#     return sum(A) + 1


def smallest_nonconstructible_value(A: List[int]) -> int:
    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
