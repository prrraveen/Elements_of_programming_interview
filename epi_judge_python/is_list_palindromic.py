from doubly_list_node import DoublyListNode
from list_node import ListNode
from test_framework import generic_test

def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next
    return True

def is_doubly_list_a_palindrome(head: DoublyListNode, tail: DoublyListNode) -> bool:
    def length(ls: DoublyListNode) -> int:
        result = 0
        while ls:
            result += 1
            ls = ls.next
        return result

    size = length(head)

    for _ in range(size//2):
        if head.data != tail.data:
            return False
        head, tail = head.next, tail.next
    return True

a = DoublyListNode(3, prev=None)
b = DoublyListNode(5, prev=a)
c = DoublyListNode(3, prev=b)
a.next, b.next = b , c
print(F"is_doubly_list_a_palindrome(a, c) = {is_doubly_list_a_palindrome(a, c)}")

# xs = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
# is_linked_list_a_palindrome(xs)
#
#
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('is_list_palindromic.py',
#                                        'is_list_palindromic.tsv',
#                                        is_linked_list_a_palindrome))