from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def _has_path_sum(node, partial_path_sum=0):
        if not node:
            return False
        if not node.left and not node.right and partial_path_sum + node.data == remaining_weight: # check if its a leaf node
            return True
        return (_has_path_sum(node.left, partial_path_sum + node.data) or
                   _has_path_sum(node.right, partial_path_sum + node.data))

    return _has_path_sum(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
