import collections
from typing import List
from test_framework import generic_test

def get_max_trapped_water(heights: List[int]) -> int:
    left, right, max_water = 0, len(heights) - 1, 0
    while left < right:
        width = right - left
        max_water = max(max_water, width * min(heights[left], heights[right]))
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_water


# def get_max_trapped_water(heights: List[int]) -> int:
#     max_so_far = float('-inf')
#     for i in range(len(heights)):
#         for j in range(i, len(heights)):
#             max_so_far = max(max_so_far, (j - i) * min(heights[i], heights[j]))
#     return max_so_far

# def get_max_trapped_water(heights: List[int]) -> int:
#     def max_between_intervals(left, mid, right):
#         left_tallest_idx = mid
#         i = mid
#         while i >= left:
#             if heights[i] >= heights[left_tallest_idx]:
#                 left_tallest_idx = i
#             # else:
#             #     break
#             i -= 1
#
#         i = mid + 1
#         right_tallest_idx = mid + 1
#         while i <= right:
#             if heights[i] >= heights[right_tallest_idx]:
#                 right_tallest_idx = i
#             # else:
#             #     break
#             i += 1
#         return ((right_tallest_idx - left_tallest_idx)
#                 * min(heights[right_tallest_idx], heights[left_tallest_idx]))
#
#
#     def _get_max_trapped_water(left, right):
#         print(F"left, right = {left, right}")
#         if left >= right:
#             return 0
#         if right - left == 1:
#             return (right - left) * min(heights[left], heights[right])
#
#         mid = (right + left) // 2
#
#         return max(
#             _get_max_trapped_water(left, mid),
#             _get_max_trapped_water(mid+1, right),
#             max_between_intervals(left, mid, right)
#         )
#
#     result =  _get_max_trapped_water(0, len(heights) - 1)
#     print(F"result = {result}")
#     return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
