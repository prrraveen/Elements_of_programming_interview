import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_depth(node: BinaryTreeNode):
        result = 0
        while node:
            result += 1
            node = node.parent
        return result

    depth0, depth1 = get_depth(node0), get_depth(node1)

    if depth0 < depth1: # make the node0 as the deeper one.
        node0, node1 = node1, node0

    for _ in range(abs(depth1 - depth0)):
        node0 = node0.parent

    while node0 and node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0





@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
