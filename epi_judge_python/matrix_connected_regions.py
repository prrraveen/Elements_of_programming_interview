import collections
from typing import List

from test_framework import generic_test

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]


# WHITE, BLACK = 0, 1
#
# def flip_color(start_x: int, start_y: int, image: List[List[bool]]) -> None:
#     color = image[start_x][start_y]
#
#     image[start_x][start_y] = 1 - color # flip its color
#
#     for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#         new_x, new_y = start_x + dx, start_y + dy
#
#         if (0 <= new_x < len(image)
#                 and 0 <= new_y < len(image[new_x])
#                 and image[new_x][new_y] == color):
#             flip_color(new_x, new_y, image)

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
    color = image[x][y]
    n = len(image)
    q = collections.deque([Coordinate(x, y)])
    image[x][y]  = 1 - image[x][y]
    while q:
        x, y = q.popleft()
        for d in (-1, 0), (0, 1), (1, 0), (0, -1):
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < n and 0 <= next_y < n and image[next_x][next_y] == color:
                image[next_x][next_y] = 1 - image[next_x][next_y]
                q.append(Coordinate(next_x, next_y))



def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
