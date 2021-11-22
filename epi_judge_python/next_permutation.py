from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # find the first entry from right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return [] # perm is the last permutation

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
