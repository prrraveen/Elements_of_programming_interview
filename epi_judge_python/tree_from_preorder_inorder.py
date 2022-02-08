import collections
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# def binary_tree_from_preorder_inorder(preorder: List[int],
#                                       inorder: List[int]) -> BinaryTreeNode:
#     node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
#     def f(left: int, right: int):
#         if left > right:
#             return None
#         elem = preorder.popleft()
#         idx = node_to_inorder_idx[elem]
#         tree = BinaryTreeNode(elem, f(left, idx - 1), f(idx + 1, right))
#         return tree
#
#     preorder = collections.deque(preorder)
#     return f(left=0, right=len(inorder) - 1)

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    def f(pre_start, pre_end, in_start, in_end):
        if pre_end < pre_start or in_end < in_start:
            return None
        idx = node_to_inorder_idx[preorder[pre_start]]
        size = idx - in_start
        # print(F"size = {size}")
        # print(F"idx = {idx}")
        return BinaryTreeNode(preorder[pre_start],
                              f(pre_start + 1, pre_start + size, in_start, in_start + size - 1),
                              f(pre_start+size+1, pre_end, in_start + size + 1, in_end))
    return f(0, len(preorder) - 1, 0, len(inorder) - 1)

def binary_tree_from_postorder_inorder(postorder: List[int],
                                       inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    def f(post_start, post_end, in_start, in_end):
        if post_end < post_start or in_end < in_start:
            return None
        idx = node_to_inorder_idx[postorder[post_end]]
        size = idx - in_start
        # print(F"size = {size}")
        # print(F"idx = {idx}")
        return BinaryTreeNode(postorder[post_end],
                              f(post_start, post_start + size - 1, in_start, in_start + size - 1),
                              f(post_start+size, post_end - 1, in_start + size + 1, in_end))
    return f(0, len(postorder) - 1, 0, len(inorder) - 1)

def inorder_traverse(tree):
    def _inorder(tree):
        if tree:
            _inorder(tree.left)
            result.append(tree.data)
            _inorder(tree.right)
    result = []
    _inorder(tree)
    return result

def preorder_traverse(tree):
    def _preorder(tree):
        if not tree:
            result.append(None)
            return
        result.append(tree.data)
        _preorder(tree.left)
        _preorder(tree.right)
    result = []
    _preorder(tree)
    return result

def postorder_traverse(tree):
    def _postorder(tree):
        if not tree:
            result.append(None)
            return
        _postorder(tree.left)
        _postorder(tree.right)
        result.append(tree.data)
    result = []
    _postorder(tree)
    return result


inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
preorder =['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
# postorder = ['F', 'A', 'E', 'B', 'I', 'G', 'D', 'C', 'H']
output = binary_tree_from_preorder_inorder(preorder, inorder)
# output = binary_tree_from_postorder_inorder(postorder, inorder)
# print(F"inorder_traverse(output) = {inorder_traverse(output)}")
print(F"preorder_traverse(output) = {preorder_traverse(output)}")
print(F"postorder_traverse(output) = {postorder_traverse(output)}")

# def make_tree(xs: List[int]) -> BinaryTreeNode:
#     def f(left: int, right: int) -> BinaryTreeNode:
#         print('*' * 10)
#         print(F"left, right = {left, right}")
#         if left == right:
#             return BinaryTreeNode(xs[left])
#         if right < left:
#             return None
#         print(F"xs[left:right+1] = {xs[left:right+1]}")
#         m = max(xs[left:right + 1])
#         idx = xs[left: right+1].index(m)
#         print(F"m, idx = {m, idx}")
#         return BinaryTreeNode(m, f(left, left + idx - 1), f(left + idx+1, right))
#     return f(0, len(xs) - 1)
#
# xs = [3, 7, 9, 2, 5, 14, 8, 16, 19, 15, 4, 1, 6, 10]
# # xs  = [2, 9, 8]
# output = make_tree(xs)
# print(F"inorder_traverse(output) = {inorder_traverse(output)}")
# print(F"preorder_traverse(output) = {preorder_traverse(output)}")
# print(F"postorder_traverse(output) = {postorder_traverse(output)}")


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('tree_from_preorder_inorder.py',
#                                        'tree_from_preorder_inorder.tsv',
#                                        binary_tree_from_preorder_inorder))