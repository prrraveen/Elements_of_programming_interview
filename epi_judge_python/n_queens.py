from typing import List
from test_framework import generic_test


def n_queens(n: int) -> [[int]]:
    def non_attacking(col: int, row: int) -> bool:
        return all(
            abs(c - col) not in (0, row - i)
            for i, c in enumerate(col_placement[:row])
        )

    def solve_n_queens(row):
        if row == n: # we found a solution
            result.append(col_placement[:])
            return
        for col in range(n):
            if non_attacking(col, row):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result

print(F"n_queens(4) = {n_queens(4)}")


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
