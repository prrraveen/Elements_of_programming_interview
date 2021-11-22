import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

# def dutch_flag_partition(pivot_index, A):
#     pivot = A[pivot_index]
#     smaller = 0
#     for i in range(len(A)):
#         if A[i] < pivot:
#             A[i], A[smaller] = A[smaller], A[i]
#             smaller += 1
#
#     larger = len(A) - 1
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         elif A[i] > pivot:
#             A[i], A[larger] = A[larger], A[i]
#             larger -= 1
# def dutch_flag_partition(pivot_index, A):
#     pivot = A[pivot_index]
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             if A[j] < pivot:
#                 A[j], A[i] = A[i], A[j]
#
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         for j in reversed(range(i)):
#             if A[j] > pivot:
#                 A[i], A[j] = A[j], A[i]
#                 break







# def dutch_flag_partition(pivot_index, xs):
#     def part(left, right):
#         if left >= right:
#             return
#         pivot_elem = xs[right]
#         first_bigger_idx = left
#         for i in range(left, right):
#             if xs[i] <= pivot_elem:
#                 xs[i], xs[first_bigger_idx] = xs[first_bigger_idx], xs[i]
#                 first_bigger_idx += 1
#         xs[right], xs[first_bigger_idx] = xs[first_bigger_idx], xs[right]
#
#         put_eql_here_idx, i =  first_bigger_idx - 1, 0
#         while i < first_bigger_idx:
#             if xs[i] == xs[first_bigger_idx]:
#                 xs[i], xs[put_eql_here_idx] = xs[put_eql_here_idx], xs[i]
#                 put_eql_here_idx -= 1
#             else:
#                 i += 1
#         # part(left, first_bigger_idx - 1)
#         # part(first_bigger_idx + 1, right)
#
#     # move the piviot element to the last
#     xs[-1], xs[pivot_index] = xs[pivot_index], xs[-1]
#     print()
#     print(F"xs = {xs}")
#     part(0, len(xs) - 1)
#     print(F"xs = {xs}")



@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
