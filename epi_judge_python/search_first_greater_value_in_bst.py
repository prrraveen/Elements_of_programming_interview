from typing import Optional

from bst_node import BstNode as B
from test_framework import generic_test

def in_order(node, key):
    if node is None:
        return None
    left = in_order(node.left, key)
    return left or node if node.data > key else None or in_order(node.right, key)



def find_first_greater_than_k(tree: B, k: int) -> Optional[B]:
    result = None
    if tree:
        result = in_order(tree, k)

    return result

def bst_to_sorted_list(tree):
    if tree:
        bst_to_sorted_list(tree.left)
        print(tree.data)
        bst_to_sorted_list(tree.right)


# root = B(19, B(7, B(3, B(2), B(5)), B(11, None, B(17, B(13)))), B(43, B(23, None, B(37, B(29, None, B(31)), B(41))), B(47, None, B(53))))
# bst_to_sorted_list(root)
# print("**" * 10)
# print(find_first_greater_than_k(root, 40))
# # print(search_key(root, 37))


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))