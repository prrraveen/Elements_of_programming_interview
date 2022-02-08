from typing import List
from test_framework import generic_test
import bisect


# def search_first_of_k(arr: List[int], key: int) -> int:
#     # if the array is empty of the element doesn't exist in the list return
#     if arr and arr[0] <=  key <= arr[-1] and arr[bisect.bisect_left(arr, key)] == key:
#         return bisect.bisect_left(arr, key)
#     return -1

def search_first_of_k(arr: List[int], key: int) -> int:
    result, left, right = -1, 0, len(arr) - 1

    while  left <= right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid - 1
        elif arr[mid] == key:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


# def first_greater_key(arr: List[int], key: int) -> int:
#     result, left, right = -1, 0, len(arr) - 1
#
#     while  left <= right:
#         mid = (left + right) // 2
#         if arr[mid] > key:
#             right = mid - 1
#         elif arr[mid] == key:
#             result = mid
#             left = mid + 1
#         else:
#             left = mid + 1
#
#     return right + 1

def interval_enclosing_k(xs, key):
    bisect_left = bisect.bisect_left(xs, key)
    bisect_right = bisect.bisect_right(xs, key)
    print(F"len(xs) = {len(xs)}")
    bisect_right -= 1
    print(F"bisect_left, bisect_right = {bisect_left, bisect_right}")
    if bisect_left == len(xs) or bisect_right == -1:
        return [-1, -1]
    # print(F"bisect_left, xs[bisect_left] = {bisect_left, xs[bisect_left]}")
    # print(F"bisect_right, xs[bisect_right] = {bisect_right, xs[bisect_right]}")


xs = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13]
output = interval_enclosing_k(xs, key=-10)
print(F"output = {output}")


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('search_first_key.py',
#                                        'search_first_key.tsv',
#                                        search_first_of_k))