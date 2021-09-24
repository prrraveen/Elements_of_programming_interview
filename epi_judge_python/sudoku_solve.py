import copy
import functools
import itertools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment) -> bool:
    return True
    # size = len(partial_assignment)
    # for row in partial_assignment:
    #     temp = []
    #     for cell in row:
    #         if cell != 0:
    #             temp.append(cell)
    #     if len(temp) != len(set(temp)):
    #         return False
    #
    # for col_index in range(size):
    #     temp = []
    #     for row_index in range(size):
    #         cell = partial_assignment[row_index][col_index]
    #         if cell != 0:
    #             temp.append(cell)
    #         if len(temp) != len(set(temp)):
    #             return False

    # for row_i, col_i in itertools.product([0, 3, 6], [0, 3, 6]):
    #     temp = []
    #     for i in range(row_i, row_i + 3):
    #         for j in range(col_i, col_i + 3):
    #             cell = partial_assignment[i][j]
    #             if cell != 0:
    #                 temp.append(cell)
    #             if len(temp) != len(set(temp)):
    #                 return False
    # return True


# partial_assignment = [[0, 3, 2, 0, 0, 0, 8, 0, 4], [8, 0, 0, 2, 0, 0, 0, 7, 0], [0, 1, 7, 0, 0, 5, 9, 0, 6],
#                      [5, 8, 0, 0, 2, 0, 0, 3, 0], [0, 0, 6, 0, 4, 0, 7, 0, 0], [0, 0, 4, 9, 1, 3, 0, 6, 0],
#                      [0, 0, 0, 7, 3, 0, 2, 0, 0], [0, 5, 9, 0, 0, 0, 0, 0, 1], [1, 0, 0, 8, 0, 9, 0, 0, 0]]
#
# print(solve_sudoku(partial_assignment))

def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0  # Starts a row.
            j += 1
            if j == len(partial_assignment[i]):
                return True  # Entire matrix has been filled without conflict.

        # Skips nonempty entries.
        if partial_assignment[i][j] != empty_entry:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            # Check row constraints.
            if any(val == partial_assignment[k][j]
                   for k in range(len(partial_assignment))):
                return False

            # Check column constraints.
            if val in partial_assignment[i]:
                return False

            # Check region constraints.
            region_size = int(math.sqrt(len(partial_assignment)))
            I = i // region_size
            J = j // region_size
            return not any(
                val == partial_assignment[region_size * I +
                                          a][region_size * J + b]
                for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment) + 1):
            # It's substantially quicker to check if entry val with any of the
            # constraints if we add it at (i,j) adding it, rather than adding it and
            # then checking all constraints. The reason is that we know we are
            # starting with a valid configuration, and the only entry which can
            # cause a problem is entry val at (i,j).
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True
        partial_assignment[i][j] = empty_entry  # Undo assignment.
        return False

    empty_entry = 0
    return solve_partial_sudoku(0, 0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
