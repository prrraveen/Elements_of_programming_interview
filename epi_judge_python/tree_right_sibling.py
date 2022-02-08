import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


# def construct_right_sibling(tree: BinaryTreeNode) -> None:
#     if not tree:
#         return None
#
#     def link(xs):
#         curr = xs[0]
#         for i in range(1, len(level)):
#             curr.next = xs[i]
#             curr = xs[i]
#
#     level = collections.deque([tree.left, tree.right]) if tree.left and tree.right else []
#     while level:
#         link(level)
#         next_level = []
#         last = None
#         while level:
#             node = level.popleft()
#             if node.left and node.right:
#                 next_level += [node.left, node.right]
#         level += next_level

# def construct_right_sibling(tree: BinaryTreeNode) -> None:
#     def populate_children_next_field(start_node):
#         while start_node and start_node.left:
#             start_node.left.next = start_node.right
#             start_node.right.next = start_node.next and start_node.next.left
#             start_node = start_node.next
#
#     while tree and tree.left:
#         populate_children_next_field(tree)
#         tree = tree.left

def construct_right_sibling(tree: BinaryTreeNode) -> None:
    if not tree:
        return
    def connect(xs: List[BinaryTreeNode]):
        for i in range(0, len(xs) - 1):
            xs[i].next = xs[i+1]

    xs = [tree]
    while xs:
        connect(xs)
        xs = [child for curr in xs for child in (curr.left, curr.right) if child]


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
