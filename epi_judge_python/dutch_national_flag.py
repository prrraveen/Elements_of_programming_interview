import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, xs: List[int]) -> None:
    # pivot = A[pivot_index]
    # smaller = 0
    # print(pivot_index,pivot,A)
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[smaller] = A[smaller], A[i]
    #         smaller += 1
    # larger = len(A) - 1
    # for i in reversed(range(len(A))):
    #     if A[i] < pivot:
    #         break
    #     elif A[i] > pivot:
    #         A[i], A[larger] = A[larger], A[i]
    #         larger -= 1
    # print(A)
    xs[pivot_index], xs[-1] = xs[-1], xs[pivot_index]
    p_index = len(xs) - 1
    i = 0
    first_high = 0
    while i < p_index:
        if xs[i] < xs[p_index]:
            xs[i], xs[first_high]  = xs[first_high], xs[i]
            first_high += 1
            i += 1
        elif xs[i] == xs[p_index]:
            xs[i], xs[p_index - 1] = xs[p_index - 1], xs[i]
            p_index -= 1
        else:
            i += 1
    for i, v in enumerate(xs[p_index:]):
        xs[p_index + i], xs[first_high + i] = xs[first_high + i], xs[p_index + i]

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
