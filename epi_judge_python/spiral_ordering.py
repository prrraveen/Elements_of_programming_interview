import collections


def matrix_in_spiral_order(xs):
    def matrix_layer_in_clock(offset, result):
        if offset == len(xs) - offset - 1:
            result.append(xs[offset][offset])
            return
        result += xs[offset][offset: -1 - offset]
        result += list(zip(*xs))[-1 - offset][offset: -1 - offset]
        result += xs[-1 - offset][-1 - offset:offset: -1]
        result += list(zip(*xs))[offset][-1 - offset: offset: -1]

    result = []
    for offset in range((len(xs) + 1) // 2):
        matrix_layer_in_clock(offset, result)
    return result


# def matrix_in_spiral_order(xs):
#     size = len(xs)
#     n = size - 1
#     res = []
#     Cell = collections.namedtuple('Cell', ('r', 'c'))
#
#     for row in xs:
#         print(row)
#
#
#     for i in range(n // 2 + 1):
#         a = Cell(i, i)
#         b = Cell(i, n - i)
#         c = Cell(n - i, n - i)
#         d = Cell(n - i, i)
#         res += [xs[row][col] for col in range(a.c, b.c + 1) for row in range(a.r, b.r + 1)]
#         res += ([xs[row][col] for col in range(b.c, c.c + 1) for row in range(b.r, c.r + 1) if row != i])
#         res += [xs[row][col] for col in reversed(range(d.c, c.c + 1)) for row in range(c.r, d.r + 1) if col != c.c]
#         res += [xs[row][col] for col in range(a.c, d.c + 1) for row in reversed(range(a.r, d.r + 1)) if row != a.r and row != d.r]
#
#         # print(F"A,b,c,d = {a,b,c,d}")
#     return res

xs = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
res = matrix_in_spiral_order(xs)
print(F"Res = {res}")


from typing import List

from test_framework import generic_test


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
