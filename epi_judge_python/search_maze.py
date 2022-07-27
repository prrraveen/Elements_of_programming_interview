import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

WHITE, BLACK = range(2)


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate):
    n, m = len(maze), len(maze[0])

    def _search_maze(node):
        if node == e:
            return True
        if node in visited:
            return False

        visited.add(node)
        return any([
            _search_maze(Coordinate(node.x + d[0], node.y + d[1])) for d in ((-1, 0), (0, 1), (1, 0), (0, -1)) if (
                0 <= node.x + d[0] < n and 0 <= node.y + d[1] < m and maze[node.x + d[0]][node.y + d[1]] == WHITE
            )
        ])

    visited = set()
    return _search_maze(s)


# maze =  [[0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0],
#        [1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0],
#        [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0],
#        [0, 0, 0, 1, 1]]
#
# s =  Coordinate(8, 3)
# e = Coordinate(17, 1)
# print(F"search_maze(maze, s, e) = {search_maze(maze, s, e)}")


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
