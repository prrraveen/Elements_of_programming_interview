import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(xs):
    left, right = 0, len(xs) - 1
    while left < right:
        while left < len(xs) and xs[left] % 2 != 1:
            left += 1
        while right >= 1 and xs[right] % 2 != 0:
            right -= 1
        if left < right:
            xs[left], xs[right] = xs[right], xs[left]


# xs = [1, 7, 3, 2, 5, 6, 7, 1, 5, 3, 2, 17]
xs = [2, 0, 4, 2]
print(F"Xs = {xs}")
even_odd(xs)
print(F"Xs = {xs}")


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
