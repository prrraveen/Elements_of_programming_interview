from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(xs: List[int], ys: List[int]) -> List[int]:
    i = 0
    j = 0
    result = []
    temp = None
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            i += 1
        elif xs[i] > ys[j]:
            j += 1
        else:
            if temp != xs[i]:
                temp = xs[i]
                result.append(temp)
            i += 1
            j += 1
    return result
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
