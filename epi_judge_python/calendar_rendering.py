import collections
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    E = ([Endpoint(event.start, True)
          for event in A] + [Endpoint(event.finish, False) for event in A])
    E.sort(key=lambda e: (e.time, not e.is_start))

    max_num_simultaneous_event, num_simultaneous_event = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_event += 1
            max_num_simultaneous_event = max(num_simultaneous_event,
                                             max_num_simultaneous_event)
        else:
            num_simultaneous_event -= 1
    return max_num_simultaneous_event

# xs = [(1,5), (4,5), (2,7), (8,9), (6,10), (11,13), (12,15), (14, 15), (9,17)]
# xs = [Event(x[0], x[1]) for x in xs]
# print(F"find_max_simultaneous_events(xs) = {find_max_simultaneous_events(xs)}")




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
