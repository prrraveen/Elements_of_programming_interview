from typing import List

from test_framework import generic_test

def cross(xs, l, m, h):
    sm = 0
    left_sum = 0
    for i in range(m, l - 1, -1):
        sm += xs[i]
        left_sum = max(sm, left_sum)

    sm = 0
    right_sum = 0
    for i in range(m + 1, h):
        sm += xs[i]
        right_sum = max(right_sum, sm)

    return max(left_sum + right_sum, left_sum, right_sum)


def sol(xs, l, h):
    if l - h == 0:
        return max(xs[l], 0)

    print(l, h)

    m = (h + l) // 2

    return max(
        sol(xs, l, m),
        sol(xs, m + 1, h),
        cross(xs, l, m, h)
    )


def find_maximum_subarray(xs: List[int]) -> int:
    return sol(xs, 0, len(xs))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
