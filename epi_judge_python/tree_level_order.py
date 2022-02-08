import collections
from typing import List
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# BalancedStatusWithHeight = collections.namedtuple(
#     'BalancedStatusWithHeight', ('balanced', 'height', 'node')
# )
# def check_k_balanced(tree, k):
#     def check_balanced(tree):
#         if not tree:
#             return BalancedStatusWithHeight(True, -1, None)
#
#         left_result = check_balanced(tree.left)
#         if not left_result.balanced:
#             return left_result
#
#         right_result = check_balanced(tree.right)
#         if not right_result.balanced:
#             return right_result
#
#         is_balanced = abs(left_result.height - right_result.height) < k
#         height = max(left_result.height, right_result.height) + 1
#         return BalancedStatusWithHeight(is_balanced, height, tree)
#
#     return check_balanced(tree).node

def inorder_rec(node):
    if node:
        inorder_rec(node.left)
        print(node.data)
        inorder_rec(node.right)

def inorder(node):
    stack = []
    current = node
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break


def preorder_rec(node: BinaryTreeNode):
    if not node:
        return
    print(node.data)
    preorder_rec(node.left)
    preorder_rec(node.right)

def preorder_iter(node: BinaryTreeNode):
    stack = [node]
    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def postorder(node: BinaryTreeNode):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

def postorder_iter(node: BinaryTreeNode):
    stack = []
    current = node
    while True:
        if current:
            stack.append(current)
            current = current.left
        else: # print this left most and make the
            current = stack.pop()
            print(current.data)


B = BinaryTreeNode
root = B(314, B(6, B(271, B(28), B(0)), B(561,None, B(3, B(17)))),
         B(6, B(2, None, B(1, B(401, None, B(641)), B(257))), B(271, None, B(28))))
postorder(root)
print('*' * 10)
# preorder_iter(root)


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('tree_level_order.py',
#                                        'tree_level_order.tsv',
#                                        binary_tree_depth_order))
# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     if not tree:
#         return []
#     result, queue = [], [tree]
#     dir = True
#     while queue:
#         if dir:
#             result.append([node.data for node in queue])
#         else:
#             result.append([node.data for node in reversed(queue)])
#         queue = [child for curr in queue for child in (curr.left, curr.right) if child]
#         dir = not dir
#     return result

# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     if not tree:
#         return []
#     result, queue = [], collections.deque([tree])
#     while queue:
#         result.append([node.data for node in queue])
#         next_level = []
#         while queue:
#             node = queue.popleft()
#             if node.left:
#                 next_level.append(node.left)
#             if node.right:
#                 next_level.append(node.right)
#         if next_level:
#             queue.extend(next_level)
#     return result