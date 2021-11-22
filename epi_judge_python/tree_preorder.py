from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    result, stack = [], []
    stack = [tree]
    while stack:
        tree = stack.pop()
        result.append(tree.data)
        if tree.right:
            stack.append(tree.right)
        if tree.left:
            stack.append(tree.left)
    return result

# def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
#     def _preorder(node):
#         if not node:
#             return None
#         result.append(node.data)
#         _preorder(node.left)
#         _preorder(node.right)
#     result = []
#     _preorder(tree)
#     return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
