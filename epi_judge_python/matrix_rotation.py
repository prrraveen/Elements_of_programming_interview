from typing import List

from test_framework import generic_test


# def rotate_matrix(square_matrix: List[List[int]]) -> None:
#     if not square_matrix:
#         return square_matrix
#
#     n = len(square_matrix)
#     result = [[None for i in range(n)] for _ in range(n)]
#     result = [[None for i in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             result[i][j] = square_matrix[~j][i]
#
#     square_matrix[:] = result

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    xs = square_matrix
    def rotate(offset):
        # print(F"offset = {offset}")
        for i in range(offset, len(square_matrix) - offset - 1):
            # print(F"xs[offset][i] = {xs[offset][i]}")
            # print(F"xs[i][~offset] = {xs[i][~offset]}")
            # print(F"xs[~offset][i] = {xs[~offset][i]}")
            # print(F"xs[i][offset] = {xs[i][offset]}")
            # print(xs[offset][i], xs[i][~offset], xs[~offset][~i], xs[~i][offset])
            xs[offset][i], xs[i][~offset], xs[~offset][~i], xs[~i][offset] = (
                xs[~i][offset], xs[offset][i], xs[i][~offset], xs[~offset][~i])
    for offset in range((len(square_matrix) + 1) // 2):
        rotate(offset)

# it = iter(range(1,18))
# xs = [[next(it) for j in range(4)] for i in range(4)]
# print(F"xs = {xs}")
# for row in xs:
#     print(row)
# print(F"rotate_matrix(xs) = {rotate_matrix(xs)}")
# for row in xs:
#     print(row)

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
