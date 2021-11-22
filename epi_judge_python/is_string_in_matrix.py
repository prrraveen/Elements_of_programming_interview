from typing import List
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 S: List[int]) -> bool:
    def f(x, y, offset):
        if len(S) == offset:
            return True
        # check if (x, y) lies outside the grid
        if (0 <= x < len(grid) and 0 <= y < len(grid[x])
            and grid[x][y] == S[offset]
            and (x, y, offset) not in previous_attempt and any(
                 f(x+a, y+b, offset + 1)
                    for a, b in ((-1, 0), (1,0), (0, -1), (0, 1)))):
            return True
        previous_attempt.add((x, y, offset))
        return False

    previous_attempt = set()
    return any(
        f(i, j, 0) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
