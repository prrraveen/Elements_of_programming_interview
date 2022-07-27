import collections
import math
from binary_tree_node import BinaryTreeNode as BstNode
from test_framework import generic_test

def is_binary_tree_bst(tree: BstNode) -> bool:
    def f(tree: BstNode, lo, hi) -> bool:
        if not tree:
            return True
        left_result = f(tree.left, lo, tree.data)
        if not left_result:
            return False
        right_result = f(tree.right, tree.data, hi)
        if not right_result:
            return False

        if not lo <= tree.data <= hi:
            return False
        return True
    return f(tree, float('-inf'), float('inf'))




# def is_binary_tree_bst(tree: BstNode) -> bool:
#     def preorder(tree: BstNode, lower_bound: int, upper_bound: int) -> bool:
#         if not tree:
#             return True
#         if tree.data < lower_bound:
#             # print(F"tree.data, lower_bound = {tree.data, lower_bound}")
#             return False
#         if tree.data > upper_bound:
#             # print(F"tree.data, upper_bound = {tree.data, upper_bound}")
#             return False
#         return preorder(tree.left, lower_bound, tree.data) and preorder(tree.right, tree.data, upper_bound)
#
#     return preorder(tree, float('-inf'), float('inf'))


# root = B(500, B(450, B(400), B(550, B(200), B(600))), B(550))
# root = B(500, B(400, B(200), B(450)), B(600, B(550, B(525), B(575)), B(800)))
# print(F"is_binary_tree_bst(root) = {is_binary_tree_bst(root)}")

# def is_binary_tree_bst(tree, low_range=float('-inf'), hight_range=float('inf')) -> bool:
#     QueueEntry = collections.namedtuple('QueryEntry', ('node', 'lower', 'upper'))
#
#     bfs_queue = collections.deque([
#         QueueEntry(tree, float('-inf'), float('inf'))
#     ])
#
#     while bfs_queue:
#         front = bfs_queue.popleft()
#         if front.node:
#             if not front.lower <= front.node.data <= front.upper:
#                 return False
#             bfs_queue += [
#                 QueueEntry(front.node.left, front.lower, front.node.data),
#                 QueueEntry(front.node.right, front.node.data, front.upper)
#             ]
#
#     return True
#
# root = BstNode(19, BstNode(7, BstNode(3, BstNode(2), BstNode(5)), BstNode(11, None, BstNode(17, BstNode(13)))), BstNode(43, BstNode(23, None, BstNode(37, BstNode(29, None, BstNode(31)), BstNode(41))), BstNode(47, None, BstNode(53))))
# print(is_binary_tree_bst(root))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))