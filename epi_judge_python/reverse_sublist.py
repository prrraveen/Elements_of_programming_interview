from typing import Optional
from list_node import ListNode
from test_framework import generic_test


# def reverse_list(l):
#     dummy_head = current = ListNode(0, l)
#     prev = None
#     while current:
#         temp = current.next
#         current.next, prev= prev, current
#         current = temp
#     return prev

def reverse_k_nodes(ls, k):
    def reverse_sublist(start: int, finish: int) -> Optional[ListNode]:
        dummy_head = start_head = ListNode(0, ls)
        for _ in range(1, start):
            start_head = start_head.next

        iter = start_head.next
        for i in range(finish - start):
            temp = iter.next
            iter.next, temp.next, start_head.next = temp.next, start_head.next, temp

        return dummy_head.next

    def length(ls):
        result = 0
        while ls:
            result += 1
            ls = ls.next
        return result

    i = k
    while i < length(ls):
        ls = reverse_sublist(i - k + 1, finish=i)
        i += k
    
    print(F"ls = {ls}")





xs = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9,
    ListNode(10, ListNode(11, ListNode(12, ListNode(13, ListNode(14, ListNode(15, ListNode(16, ListNode(17)))))))))))))))))
print(xs)
# output = reverse_list(xs)
output = reverse_k_nodes(xs, 4)
print(F"output = {output}")

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('reverse_sublist.py',
#                                        'reverse_sublist.tsv', reverse_sublist))
