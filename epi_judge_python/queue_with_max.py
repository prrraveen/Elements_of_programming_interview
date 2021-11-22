import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidate_for_maximum = collections.deque()

    def enqueue(self, x: int) -> None:
        self._entries.append(x)
        while self._candidate_for_maximum and self._candidate_for_maximum[-1] < x:
            self._candidate_for_maximum.pop()
        self._candidate_for_maximum.append(x)

    def dequeue(self) -> int:
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidate_for_maximum[0]:
                self._candidate_for_maximum.popleft()
            return result
        raise IndexError('empty queue')


    def max(self) -> int:
        if self._candidate_for_maximum:
            return self._candidate_for_maximum[0]
        raise ValueError('list is empty')



def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
