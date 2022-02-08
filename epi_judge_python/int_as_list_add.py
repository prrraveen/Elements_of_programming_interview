from typing import Optional
from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L1: ListNode):
    prev = None
    current = L1
    while current:
        print(F"current = {current}")
        temp = current.next
        current.next, prev = prev, current
        current = temp
    return prev

def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    L1, L2 = reverse_sublist(L1), reverse_sublist(L2)
    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next
    return reverse_sublist(dummy_head.next)

L1 = ListNode(4, ListNode(1, ListNode(3)))
L2 = ListNode(9, ListNode(0, ListNode(7)))
print(F"add_two_numbers(L1, L2) = {add_two_numbers(L1, L2)}")

# def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
#     dummy_head = tail = ListNode(0)
#     carry = 0
#     while L1 or L2:
#         if not L2:
#             if carry:
#                 x = L1.data + carry
#                 carry = x // 10
#                 tail.next = ListNode(x % 10)
#                 L1 = L1.next
#             else: # there is no carry. copy the remaining digits and terminate
#                 tail.next = L1
#                 break
#         elif not L1:
#             if carry:
#                 x = L2.data + carry
#                 carry = x // 10
#                 tail.next = ListNode(x % 10)
#                 L2 = L2.next
#             else: # there is no carry. copy the remaining digits and terminate
#                 tail.next = L2
#                 break
#         else:
#             x = L1.data + L2.data + carry
#             carry = x // 10
#             tail.next = ListNode(x % 10)
#             L1, L2 = L1.next, L2.next
#         tail = tail.next
#     if carry:
#         tail.next = ListNode(carry)
#     return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
