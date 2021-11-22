import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def brute_search_entry_equal_to_its_index(A: List[int]) -> int:
#     for index, elem in enumerate(A):
#         if index == elem:
#             return index
#     # result = [index for index, elem in enumerate(A) if index == elem]
#     return -1

def search_entry_equal_to_its_index(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2

        if mid == A[mid]:
            return mid
        elif mid < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1



@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
