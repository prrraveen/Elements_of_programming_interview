from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next

# xs = ListNode(2, ListNode(4, ListNode(6, ListNode(13))))
# xs = ListNode(1, ListNode(3, ListNode(8, ListNode(13, ListNode(10, ListNode(12, ListNode(9)))))))
# res = even_odd_merge(xs)
# print(F"res = {res}")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
