import collections
from typing import List
from binary_tree_node import BinaryTreeNode as Bi
from test_framework import generic_test

def check_binary_tree_is_height_balanced(tree):
    IsBalancedWithHeight = collections.namedtuple('IsBalancedWithHeight', ('isBalanced', 'height'))
    def f(tree: Bi) -> IsBalancedWithHeight:
        if not tree:
            return IsBalancedWithHeight(True, 0)

        left_result = f(tree.left)

        if not left_result.isBalanced:
            return left_result

        right_result = f(tree.right)

        if not right_result.isBalanced:
            return right_result

        if abs(left_result.height - right_result.height) > 1:
            return IsBalancedWithHeight(False, -1)

        return IsBalancedWithHeight(True, 1 + max(left_result.height, right_result.height))

    return f(tree)




# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
#                                        preorder_traversal))

xs =  Bi('H',
         Bi('J'),
         Bi('K',
            Bi('L'),
            Bi('M', Bi('N'))
            ))

xs =  Bi('H',
         Bi('J'),
         Bi('K',
            Bi('L'),
            Bi('M')
            ))
# xs = Bi('H')

print(F"get_height(xs) = {check_binary_tree_is_height_balanced(xs)}")