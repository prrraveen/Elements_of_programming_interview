from typing import List
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    s, result = [], []
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result



# def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
#     def _inorder(node):
#         if not node:
#             return
#         _inorder(node.left)
#         result.append(node.data)
#         _inorder(node.right)
#     result = []
#     _inorder(tree)
#     return result
#

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
