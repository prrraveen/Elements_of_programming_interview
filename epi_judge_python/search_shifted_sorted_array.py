import math
from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        if right - left == 1:
            return right
        print(F"left, right = {left, right}")
        print(F"A[left], A[right] = {A[left], A[right]}")
        mid = (left + right) // 2
        if A[mid] > A[right]: # Its not increasing subsequence. So the dipression should be in it
            left = mid
        else:
            right = mid
    return right




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
