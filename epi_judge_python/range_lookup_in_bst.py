import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


# def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
#     def in_order(tree):
#         if not tree:
#             return
#         in_order(tree.left)
#         if interval.left <= tree.data <= interval.right:
#             result.append(tree.data)
#         in_order(tree.right)
#
#     result = []
#     in_order(tree)
#     return result

def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:

    def f(tree):
        if not tree:
            return
        if interval.left <= tree.data <= interval.right:
            f(tree.left)
            result.append(tree.data)
            f(tree.right)
        elif tree.data > interval.left:
            f(tree.left)
        else:
            f(tree.right)

    result = []
    f(tree)
    return result

def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
