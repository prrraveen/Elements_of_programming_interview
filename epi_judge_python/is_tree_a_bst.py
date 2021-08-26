import collections
import math

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    QEntry = collections.namedtuple('QEntry', ('node', 'lower', 'upper'))
    bfs_q = collections.deque([QEntry(tree, float('-inf'), float('inf'))])

    while bfs_q:
        front = bfs_q.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_q += [
                QEntry(front.node.left, front.lower, front.node.data),
                QEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

def inorder(root):
    if not root:
        return True
    inorder(root.left)
    print(root.data)
    inorder(root.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))