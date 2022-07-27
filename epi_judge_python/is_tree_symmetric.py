from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    def f(A: BinaryTreeNode, B: BinaryTreeNode) -> bool:
        if not A and not B:
            return True
        if A and not B:
            return False
        if B and not A:
            return False

        return all([A.data == B.data, f(A.left, B.right), f(A.right, B.left)])

    return f(tree.left, tree.right)


# def is_symmetric(tree: BinaryTreeNode) -> bool:
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
