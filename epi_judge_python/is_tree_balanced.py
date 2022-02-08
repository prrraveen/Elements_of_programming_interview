import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    NodesHeightWithBalance = collections.namedtuple('NodesHeightWithBalance', ('height', 'isBalanced'))
    def f(node):
        if not node:
            return NodesHeightWithBalance(-1, True)
        left_result = f(node.left)
        if not left_result.isBalanced:
            return NodesHeightWithBalance(0, False)

        right_result = f(node.right)
        if not right_result.isBalanced:
            return NodesHeightWithBalance(0, False)

        isBalanced = abs(left_result.height - right_result.height) <= 1
        return NodesHeightWithBalance(max(left_result.height, right_result.height) + 1, isBalanced)

    output = f(tree)
    print(F"output = {output}")
    return output.isBalanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
