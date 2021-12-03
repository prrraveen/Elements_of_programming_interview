from typing import Optional
from doubly_list_node import DoublyListNode
from list_node import ListNode
from test_framework import generic_test



def merge_two_sorted_lists(xs: Optional[DoublyListNode],
                           ys: Optional[DoublyListNode]) -> Optional[DoublyListNode]:
    zs = dummy_head = ListNode(0, None)
    while xs and ys:
        if xs.data < ys.data:
            zs.next, xs.prev, xs = xs, zs, xs.next
        else:
            zs.next, ys.prev, ys = ys, zs, ys.next
        zs = zs.next

    if xs:
        zs.next, xs.prev = xs, zs

    if ys:
        zs.next, ys.prev = ys, zs

    dummy_head.next.prev = None
    return dummy_head.next

a = DoublyListNode(3, prev=None)
b = DoublyListNode(5, prev=a)
c = DoublyListNode(7, prev=b)
a.next, b.next = b , c
print(F"a = {a}")

eight = DoublyListNode(3, prev=None)
three = DoublyListNode(4, prev=eight)
four = DoublyListNode(8, prev=three)
eight.next, three.next = three, four
print(F"eight = {eight}")
output  = merge_two_sorted_lists(a, eight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
