from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    p2 = dummy_head.next
    for _ in range(k):
        p2 = p2.next

    p1 = dummy_head

    while p2:
        p1, p2 = p1.next, p2.next
    p1.next = p1.next.next
    return dummy_head.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
