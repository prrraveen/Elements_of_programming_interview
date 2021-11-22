from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from successor_in_tree import find_successor


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    result = []
    while tree.left:
        tree = tree.left

    while tree:
        result.append(tree.data)
        tree = find_successor(tree)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
