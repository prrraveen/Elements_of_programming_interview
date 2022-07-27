import itertools
from copy import copy
from typing import List
from test_framework import generic_test, test_utils

# def permutations(A):
#     return list(map(list, itertools.permutations(A)))

def permutations(A):
    n = len(A)
    def f(rem, partial_count):

        if len(partial_count) == n:
            result.append(copy(partial_count))
        for i in range(len(rem)):
            f(rem[:i] + rem[i+1:], partial_count + [rem[i]])
    result = []
    f(A, [])
    return result

xs = [1, 2, 3]
print(F"permutations(xs) = {permutations(xs)}")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))