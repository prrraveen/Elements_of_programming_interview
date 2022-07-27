from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0
    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:
        print(F"partial_path_sum = {partial_path_sum}")
        return partial_path_sum
    return sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum)

# def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
#     def map_parents_mark_lifts(node, parent=None):
#         if not node:
#             return
#         map_parents_mark_lifts(node.left, parent=node)
#         if not node.left and not node.right:
#             leafs.append(node)
#         if parent:
#             parent_map[id(node)] = parent
#         map_parents_mark_lifts(node.right, parent=node)
#
#     leafs, parent_map = [], {}
#     map_parents_mark_lifts(tree)
#
#     bins = []
#     for node in leafs:
#         partial_path_sum = ''
#         while id(node) in parent_map:
#             partial_path_sum += str(node.data)
#             node = parent_map[id(node)]
#         bins.append(partial_path_sum)
#     print(F"bins = {bins}")
#     # return sum(bins)


# def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
#     def f(node):
#         if node is None:
#             return ['']
#         left_result = f(node.left)
#         right_result = f(node.right)
#         print(F"node.data = {node.data}")
#         print(F"left_result = {left_result}")
#         print(F"right_result = {right_result}")
#         left_number = [str(node.data) + x for x in left_result]
#         right_number = [str(node.data) + x for x in right_result]
#         print(F"left_number = {left_number}")
#         print(F"right_result = {right_number}")
#         return left_number + right_number
#
#     result = f(tree)
#     print(F"result = {result}")
#     xs = [int(x[::-1], 2) for x in result]
#     print(F"xs = {xs}")
#     return sum(xs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
