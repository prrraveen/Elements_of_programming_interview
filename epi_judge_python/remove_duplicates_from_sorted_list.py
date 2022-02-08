from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# def remove_duplicates(L: ListNode) -> Optional[ListNode]:
#     if not L:
#         return L
#     current = L
#     while current.next:
#         if current.data == current.next.data:
#             current.next = current.next.next
#         else:
#             current = current.next
#
#     return L

def remove_more_than_m(L: ListNode, m: int) -> Optional[ListNode]:
    if not L:
        return L
    dummy_head = prev = ListNode(0, L)
    start, end = L, L.next
    counter = 1
    while end:
        if end.data == start.data:
            counter += 1
        else:
            if counter >= m:
                prev.next, start = end, end
            prev, start = start, end
            counter = 1
        end = end.next

    if counter >= m:
        prev.next, start = end, end

    return dummy_head.next

L = ListNode
# xs = L(1, L(1, L(1, L(2, L(2, L(3, L(3, L(3, L(4, L(4, L(4, L(4, L(5, L(6, L(7)))))))))))))))
xs = L(1, L(1, L(1, L(4, L(5, L(6, L(6, L(6, L(6)))))))))
# xs = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3,  ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))))))))
print(F"xs = {xs}")
output = remove_more_than_m(xs, 3)
print(F"output = {output}")


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main(
#             'remove_duplicates_from_sorted_list.py',
#             'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
