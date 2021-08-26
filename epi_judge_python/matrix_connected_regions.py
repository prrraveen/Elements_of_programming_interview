from typing import List

from test_framework import generic_test

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def flip_color(start_x: int, start_y: int, image: List[List[bool]]) -> None:
    result, stack = [], [(start_x, start_y)]
    color = image[start_x][start_y]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= len(image):
            continue

        if y < 0 or y >= len(image[x]):
            continue

        # print(color, image[x][y])
        if image[x][y] != color: # avoid using return and continue
            continue

        image[x][y] = 1 - image[x][y] # Anki flip 1 to 0 and 0 to 1

        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x = x + d[0]
            next_y = y + d[y]
            stack.append((next_x, next_y))


def _flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    image[x][y] = 1 - image[x][y]
    for d in (0, 1), (0, -1), (1, 0), (-1, 0):
        next_x, next_y = x + d[0], y + d[1]
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
            and image[next_x][next_y] == color):
            _flip_color(next_x, next_y, image)




def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
