import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# xs = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11, ListNode(12, ListNode(13, ListNode(14, ListNode(15, ListNode(16, ListNode(17)))))))))))))))))
# tail = xs
# while tail.next:
#     tail = tail.next
#
# start_of_cycle = xs
# for _ in range(1, 5):
#     start_of_cycle = start_of_cycle.next
#
# tail.next = start_of_cycle

def has_cycle(head: ListNode) -> Optional[ListNode]:
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


def _has_cycle(head: ListNode) -> Optional[ListNode]:
    def get_cycle_len(node):
        current = node.next
        result = 1
        while current is not node:
            result, current = result + 1, current.next
        return result

    first = second = head
    while second and second.next and second.next.next:
        first, second = first.next, second.next.next
        if second is first:
            second = head
            for _ in range(get_cycle_len(first)):
                second = second.next

            first = head
            while first is not second:
                first, second = first.next, second.next

            return first

    return None



@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))