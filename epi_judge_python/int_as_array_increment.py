import functools
from typing import List

from test_framework import generic_test


def plus_one(xs: List[int]) -> List[int]:
    xs[-1] = xs[-1] + 1
    n = len(xs) - 1

    for i in reversed(range(1, len(xs))):
        if xs[i] != 10:
            break
        xs[i] = 0
        xs[i-1] += 1

    if xs[0] == 10:
        xs[0] = 1
        xs.append(0)
    return xs


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
