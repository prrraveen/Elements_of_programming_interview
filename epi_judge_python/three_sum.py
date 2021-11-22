from bisect import bisect
from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    d, n = {}, len(A)
    for x in A:
        d[x] = True
    for i in range(n):
        for j in range(n):
            x = t - (A[i] + A[j])
            if x in d:
                return True
    return False


# def has_three_sum(A: List[int], t: int) -> bool: #     A.sort()
#     n = len(A)
#     for i in range(n):
#         for j in range(n):
#             x = t - (A[i] + A[j])
#             index = bisect.bisect_left(A, x)
#             if index < n and A[index] == x:
#                 return True
#     return False

# def has_three_sum(A: List[int], t: int) -> bool:
#     A.sort()
#     n = len(A)
#     for i in range(n):
#         left = i
#         right = n - 1
#
#         while left < right:
#             pair_sum =  A[i] + A[left] + A[right]
#             if pair_sum == t:
#                 return True
#             if pair_sum < t:
#                 left += 1
#             elif pair_sum > t:
#                 right -= 1
#     return False




# print(has_three_sum([1, -1], 1))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
