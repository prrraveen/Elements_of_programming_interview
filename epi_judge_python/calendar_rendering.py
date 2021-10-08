import collections
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    max_so_far = -math.inf
    endpoints = [endpoint for interval in A for endpoint in interval]
    for endpoint in endpoints:
        count = 0
        for [start, end] in A:
            if start <= endpoint <= end:
                count += 1
        max_so_far = max(count, max_so_far)
    return max_so_far






@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
