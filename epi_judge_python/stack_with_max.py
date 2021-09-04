import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure

ElementWithMax = collections.namedtuple('ElementWithMax', ('element', 'max'))

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.last = None

    def empty(self) -> bool:
        return not self.last

    def max(self) -> int:
        if self.last:
            return self.last.data.max

    def pop(self) -> int:
        if self.last:
            temp = self.last
            self.last = self.last.prev
            return temp.data.element



    def push(self, x: int) -> None:
        if self.last:
            max_so_far = max(self.last.data.max, x) if self.last else x
            self.last.next= Node(ElementWithMax(x, max_so_far), self.last)
            self.last = self.last.next
        else:
            self.last = Node(ElementWithMax(x, x))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')

# xs = [["Stack", 0], ["push", -784], ["pop", -784], ["push", 452], ["max", 452], ["pop", 452], ["push", 761],
#       ["push", 402], ["max", 761], ["pop", 402], ["max", 761], ["pop", 761]]
#
# stack_tester(xs)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
