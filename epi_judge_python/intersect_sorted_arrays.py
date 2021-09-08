import math
from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(xs: List[int], ys: List[int]) -> List[int]:
    p1, p2 = 0, 0
    last_added, result = math.inf, []
    while p1 < len(xs) and p2 < len(ys):
        xp1 = xs[p1]
        yp2 = ys[p2]
        if xp1 < yp2:
            p1 += 1
        elif xp1 > yp2:
            p2 += 1
        else:
            if last_added != xp1:
                result.append(xp1)
            last_added = xp1
            p1 += 1
    return result
    return



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
