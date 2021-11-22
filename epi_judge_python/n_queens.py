from typing import List
from test_framework import generic_test

def n_queens(n: int) -> List[List[int]]:
    print()
    print(F"n = {n}")
    def can_place(_partial_placement, col_index):
        if col_index in _partial_placement:
            return False
        print('*'*100)
        for i, c in enumerate(_partial_placement):
            print(F"i, c, col_index = {i, c, col_index}")
        return True

    def n_queens_helper(partial_palcement):
        if len(partial_palcement) == n:
            all_placements.append(partial_palcement)
        else:
            for col_index in range(n):
                if can_place(partial_palcement, col_index):
                    n_queens_helper(partial_palcement + [col_index])


    all_placements = []
    for i in range(n):
        n_queens_helper([i])
    return all_placements

print(F"n_queens(4) = {n_queens(4)}")
# def n_queens(n: int) -> List[List[int]]:
#     def valid(col_placement, row, col):
#         print('*', 100)
#         print(col_placement, row, col)
#         for i, c in enumerate(col_placement[:row]):
#             print(F"i, c = {i, c}")
#             print(F"abs(c - col), (0, row - i) = {abs(c - col), (0, row - i)}")
#         return all(
#             abs(c - col) not in (0, row - i)
#             for i, c in enumerate(col_placement[:row]))
#
#     def solve_n_queens(row):
#         if row == n:
#             result.append(list(col_placement))
#             return
#         for col in range(n):
#             if valid(col_placement, row, col):
#                 col_placement[row] = col
#                 solve_n_queens(row + 1)
#
#     result, col_placement = [], [0] * n
#     solve_n_queens(0)
#     return result
#


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
