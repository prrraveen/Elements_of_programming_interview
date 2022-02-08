from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # we came down from prev
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif tree.left is prev:
            # we came up from the trees left child.
            result.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent

        prev, tree = tree, next
    return result

# def preorder(tree: BinaryTreeNode):
#     if tree:
#         print(tree.data)
#         preorder(tree.left)
#         preorder(tree.right)

# B = BinaryTreeNode
# root = B(314, B(6, B(271, B(28), B(0)), B(561,None, B(3, B(17)))),
#          B(6, B(2, None, B(1, B(401, None, B(641)), B(257))), B(271, None, B(28))))
#
#
# A = BinaryTreeNode(314)
# B = BinaryTreeNode(6, parent=A)
# I = BinaryTreeNode(16, parent=A)
# A.left, A.right = B, I
# preorder(root)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
