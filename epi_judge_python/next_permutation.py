from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    i = len(perm) - 1
    while i > 0:
        if perm[i] > perm[i - 1]:
            break
        i -=1
    if i == 0:
        return []
    s = i-1
    min_at = i
    for j in range(i, len(perm)):
        if perm[j] > s:
            min_at = j
        else:
            break
    print(F"min_at, perm[min_at] = {min_at, perm[min_at]}")
    print(F"s = {s}")
    perm[min_at], perm[s] = perm[s], perm[min_at]
    print(F"perm = {perm}")
    perm[:] = perm[:i] + perm[i:][::-1]



# xs = [6, 2, 1, 5, 4, 3, 0]
# print(F"next_permutation(xs) = {next_permutation(xs)}")
# print(F"xs = {xs}")



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
