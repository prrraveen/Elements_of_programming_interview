import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, xs):
    pivot = xs[pivot_index]
    smaller = 0
    for i in range(len(xs)):
        if xs[i] < pivot:
            xs[i], xs[smaller] = xs[smaller], xs[i]
            smaller += 1

    larger = len(xs) - 1
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] < pivot:
            break
        if xs[i] > pivot:
            xs[i], xs[larger] = xs[larger], xs[i]
            larger -= 1

# xs = [7,1,2,3,4,5,1]
# dutch_flag_partition(3, xs)
# print(F"Xs = {xs}")
#


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
