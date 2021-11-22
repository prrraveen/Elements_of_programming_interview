from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def add_two_numbers(xs: ListNode, ys: ListNode) -> Optional[ListNode]:
    carry = 0
    result_head = result = ListNode()
    while xs or ys or carry:
        sum = carry + (xs.data if xs else 0) + (ys.data if ys else 0)
        xs = xs.next if xs else None
        ys = ys.next if ys else None
        result.next = ListNode(sum % 10)
        carry, result = sum // 10, result.next
    return result_head.next

# def add_two_numbers(xs: ListNode, ys: ListNode) -> Optional[ListNode]:
#     carry = 0
#     result_head = result = ListNode()
#     while xs and ys:
#         sum = xs.data + ys.data + carry
#         carry, digit = sum // 10, sum % 10
#         result.next = ListNode(digit)
#         result, xs, ys = result.next, xs.next, ys.next
#
#     left_over = xs or ys
#     while carry and left_over:
#         sum = carry + left_over.data
#         carry, digit = sum // 10, sum % 10
#         result.next = ListNode(digit)
#         left_over, result = left_over.next, result.next
#
#     if carry:
#         result.next = ListNode(carry)
#     else:
#         result.next = left_over
#
#     return result_head.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
