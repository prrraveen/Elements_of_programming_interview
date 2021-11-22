import functools
from typing import List

from test_framework import generic_test

def plus_one(xs: List[int]) -> List[int]:
    xs.reverse()
    carry = 1
    i = 0
    while i < len(xs) and carry:
        new_digit = xs[i] + carry
        xs[i] = new_digit % 10
        carry = new_digit // 10
        i += 1
    if carry:
        xs.append(1)
    xs.reverse()
    return xs




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
