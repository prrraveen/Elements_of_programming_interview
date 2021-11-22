from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.primary = []
        self.secondary = []
        self.length = 0

    def enqueue(self, x: int) -> None:
        self.length += 1
        self.primary.append(x)

    def dequeue(self) -> int:
        if self.secondary:
            self.length -= 1
            return self.secondary.pop()
        elif self.primary:
            for x in reversed(self.primary):
                self.secondary.append(x)
            self.primary = []
            self.length -= 1
            return self.secondary.pop()
        else:
            raise ValueError('q is empty')

    def size(self) -> int:
        return self.length


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
