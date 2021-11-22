import math

from test_framework import generic_test


def square_root(k: float) -> float:
    left, right = (k, 1.0) if k < 1.0 else (1.0, k)

    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > k:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
