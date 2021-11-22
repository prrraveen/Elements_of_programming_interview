import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from tree_connect_leaves import create_list_of_leaves


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def root_to_left_most_leaf(tree):
        if not tree:
            return []
        if not tree.left and not tree.right:
            return []
        if tree.left:
            return [tree] +  root_to_left_most_leaf(tree.left)
        else:
            return [tree] + root_to_left_most_leaf(tree.right)

    def root_to_rigth_most_leaf(tree):
        if not tree:
            return []
        if not tree.left and not tree.right:
            return []
        if tree.right:
            return [tree] + root_to_rigth_most_leaf(tree.right)
        else:
            return [tree] + root_to_rigth_most_leaf(tree.left)

    if not tree:
        return []

    if not tree.left and not tree.right:
        return [tree]

    leaves = create_list_of_leaves(tree)
    lefts = root_to_left_most_leaf(tree.left)
    rights = root_to_rigth_most_leaf(tree.right)
    return [tree] + lefts + leaves + rights[::-1]






B = BinaryTreeNode
root = B(314, B(6, B(271, B(28), B(0)), B(561,None, B(3, B(17)))),
         B(6, B(2, None, B(1, B(401, None, B(641)), B(257))), B(271, None, B(28))))

print(F"exterior_binary_tree(root) = {exterior_binary_tree(root)}")

def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))
    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
