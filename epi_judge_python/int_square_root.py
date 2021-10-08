from test_framework import generic_test


def square_root(k: int) -> int:
    left, right = 0, k

    while left <= right:
        m = (left + right) // 2
        if m * m <= k:
            left = m + 1
        else:
            right = m - 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
