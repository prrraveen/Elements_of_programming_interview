from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    xs = [[1] * (i + 1)  for i in range(n)]
    for i in range(2, len(xs)):
        for j in range(1, len(xs[i]) - 1):
            xs[i][j] = xs[i-1][j-1] + xs[i-1][j]
    return xs


# print(F"generate_pascal_triangle(5) = {generate_pascal_triangle(5)}")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
