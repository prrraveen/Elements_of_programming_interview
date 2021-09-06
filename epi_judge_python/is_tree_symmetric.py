from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def is_sym(left, right):
        if not left and not right:
            return True

        if left and right:
            return left.data == right.data and is_sym(left.left, right.right) and is_sym(left.right, right.left)

        return False

    return is_sym(tree.left, tree.right) if tree else True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
