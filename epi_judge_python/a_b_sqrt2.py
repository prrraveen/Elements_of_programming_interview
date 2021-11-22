import math
from typing import List

import bintrees

from test_framework import generic_test


# def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
#     xs = []
#     SQRT2 = math.sqrt(2)
#     for a in range(k):
#         for b in range(k):
#             xs.append(a + b * SQRT2)
#     xs.sort()
#     return xs[:k]

class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])

    result = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)
        candidates[ABSqrt2(next_smallest.a + 1, next_smallest.b)] = None
        candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None
    return result

print(F"generate_first_k_a_b_sqrt2(2) = {generate_first_k_a_b_sqrt2(2)}")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
