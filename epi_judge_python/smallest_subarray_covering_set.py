import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(para, keys):
    class DoublyLinkedList:
        def __init__(self, data):
            self.data = data
            self.prev = self.next = None


    class LinkedList:
        def __init__(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def insert_after(self, data):
            node = DoublyLinkedList(data)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node: DoublyLinkedList):
            if node is self.head and node is self.tail:
                self.head = self.tail = None
            elif node is self.head:
                self.head = node.next
                node.next.prev = None
            elif node is self.tail:
                self.tail = self.tail.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self._size -= 1
            node.prev = node.next = None

    loc = LinkedList()
    d = {s: None for s in keys}
    result = Subarray(-1, -1)
    for idx, s in enumerate(para):
        if s in keys:
            it = d[s]
            if it is not None:
                loc.remove(it)
            loc.insert_after(idx)
            d[s] = loc.tail

            if len(loc) == len(keys):
                if (result == (-1,-1) or
                    idx - loc.head.data < result[1] - result[0]):
                    result = (loc.head.data, idx)
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))