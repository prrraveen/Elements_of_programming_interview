import itertools
from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    size = len(partial_assignment)
    for row in partial_assignment:
        temp = []
        for cell in row:
            if cell != 0:
                temp.append(cell)
        if len(temp) != len(set(temp)):
            return False

    for col_index in range(size):
        temp = []
        for row_index in range(size):
            cell = partial_assignment[row_index][col_index]
            if cell != 0:
                temp.append(cell)
            if len(temp) != len(set(temp)):
                return False

    for row_i, col_i in itertools.product([0, 3, 6], [0, 3, 6]):
        temp = []
        for i in range(row_i, row_i + 3):
            for j in range(col_i, col_i + 3):
                cell = partial_assignment[i][j]
                if cell != 0:
                    temp.append(cell)
                if len(temp) != len(set(temp)):
                    return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
