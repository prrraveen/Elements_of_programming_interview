import collections
import math

from binary_tree_node import BinaryTreeNode as BstNode
from test_framework import generic_test

def is_binary_tree_bst(tree, low_range=float('-inf'), hight_range=float('inf')) -> bool:
    QueueEntry = collections.namedtuple('QueryEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque([
        QueueEntry(tree, float('-inf'), float('inf'))
    ])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]

    return True

root = BstNode(19, BstNode(7, BstNode(3, BstNode(2), BstNode(5)), BstNode(11, None, BstNode(17, BstNode(13)))), BstNode(43, BstNode(23, None, BstNode(37, BstNode(29, None, BstNode(31)), BstNode(41))), BstNode(47, None, BstNode(53))))
print(is_binary_tree_bst(root))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))