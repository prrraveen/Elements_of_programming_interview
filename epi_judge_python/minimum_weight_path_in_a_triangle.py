from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j-1])
    result = min(triangle[-1])
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
