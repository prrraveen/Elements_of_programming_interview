import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
#     def f():
#         if not xs:
#             return
#         head, *tail = xs
#
#         xs.pop(0)
#         if head is None:
#             return
#         node = BinaryTreeNode(head)
#         node.left = f()
#         node.right = f()
#         return node
#
#     xs = preorder
#     index = [0]
#     return f()


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def f():
        i = index[0]
        if i == len(xs):
            return
        head = xs[i]

        index[0] = index[0] + 1
        if head is None:
            return
        node = BinaryTreeNode(head)
        node.left = f()
        node.right = f()
        return node

    xs = preorder
    index = [0]
    return f()

# def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
#     def f(preorder_iter):
#         subtree_key = next(preorder_iter)
#         if subtree_key is None:
#             return None
#         left_subtree = reconstruct_preorder(preorder_iter)
#         right_subtree = reconstruct_preorder(preorder_iter)
#         return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
#     return f(iter(preorder))

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
