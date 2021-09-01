from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(xs: Optional[ListNode],
                           ys: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()

    while xs and ys:
        if xs.data < ys.data:
            tail.next, xs = xs, xs.next
        else:
            tail.next, ys = ys, ys.next
        tail = tail.next

    tail.next = xs or ys
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
