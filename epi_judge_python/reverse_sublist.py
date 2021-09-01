from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(xs: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head =  ListNode(0, xs)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next



xs = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
result = reverse_sublist(xs, 3, 7)
print(F"Result = {result}")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
