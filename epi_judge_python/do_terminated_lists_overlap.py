import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
#     visited = set()
#     while l0:
#         visited.add(id(l0))
#         l0 = l0.next
#
#     while l1:
#         if id(l1) in visited:
#             return l1
#         l1 = l1.next

# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
#     while l0:
#         current = l1
#         while current:
#             if current is l0:
#                 return l0
#             current = current.next
#         l0 = l0.next

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(node):
        result = 0
        while node:
            result += 1
            node = node.next
        return result

    l0_size, l1_size = length(l0), length(l1)

    bigger, smaller = (l0, l1) if l0_size > l1_size else (l1, l0)

    diff = abs(l0_size - l1_size)

    for _ in range(diff):
        bigger = bigger.next
        
    while bigger and smaller:
        if bigger is smaller:
            return bigger
        bigger, smaller = bigger.next, smaller.next




@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
