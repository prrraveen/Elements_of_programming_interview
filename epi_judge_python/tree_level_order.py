from collections import deque
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return result

    curr_depth_node = [tree]

    while curr_depth_node:
        result.append([node.data for node in curr_depth_node])
        curr_depth_node = [
            child for curr in curr_depth_node for child in (curr.left, curr.right) if child
        ]

    return result




B = BinaryTreeNode
root = B(314, B(6, B(271, B(28), B(0)), B(561,None, B(3, B(17)))),
         B(6, B(2, None, B(1, B(401, None, B(641)), B(257))), B(271, None, B(28))))

xs = binary_tree_depth_order(root)
print(xs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
