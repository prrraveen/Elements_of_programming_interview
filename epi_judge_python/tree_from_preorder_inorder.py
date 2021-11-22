import collections
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def f(start_of_preorder, end_of_preorder, start_of_inorder, end_of_inorder):
        if end_of_preorder <= start_of_preorder or end_of_inorder <= start_of_inorder:
            return None

        root_inorder_index = node_to_inorder_idx[preorder[start_of_preorder]]
        left_subtree_size = root_inorder_index - start_of_inorder

        return BinaryTreeNode(preorder[start_of_preorder],
                              f(start_of_preorder + 1, start_of_preorder + 1 + left_subtree_size,
                                start_of_inorder, root_inorder_index),
                              f(start_of_preorder + 1 + left_subtree_size, end_of_preorder,
                                root_inorder_index + 1, end_of_inorder))

    return f(0, len(preorder), 0, len(inorder))


# inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
# preorder =['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
# preorder = collections.deque(preorder)
# print(F"binary_tree_from_preorder_inorder(preorder, inorder) = {binary_tree_from_preorder_inorder(preorder, inorder)}")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
