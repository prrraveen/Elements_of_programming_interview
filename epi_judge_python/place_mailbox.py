from collections import Counter
import functools
import random
from typing import List

Building = collections.namedtuple('Building', ('distance', 'resident'))
def place_mailbox(A: List[Building]) -> Building:
    def calc_walk_dist(xs, target: Building) -> int:
        return functools.reduce(lambda walking_distance, building:  walking_distance + building.resident * abs(
            target.distance - building.distance), xs, 0)

    def partition(left, right, pivot_idx) -> int:
        pivot_val = A[pivot_idx]
        A[right], A[pivot_idx] = A[pivot_idx], A[right]

        write_idx = left

        for i in range(left, right):
            if A[i].distance > pivot_val.distance:
                A[write_idx], A[i] = A[i], A[write_idx]
                write_idx += 1
        A[write_idx], A[right] = A[right], A[write_idx]
        return write_idx


    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        pivot_new_idx = partition(left, right, pivot_idx)
        left_count = calc_walk_dist(A[:pivot_new_idx], A[pivot_new_idx])
        right_count =  calc_walk_dist(A[pivot_new_idx:], A[pivot_new_idx])
        print(F"left_count, right_count = {left_count, right_count}")
        if left_count == right_count:
            return A[pivot_new_idx]
        elif left_count > right_count:
            right = pivot_new_idx - 1
        else:
            left = pivot_new_idx + 1


xs = [Building(6, 3), Building(3, 2), Building(1, 1), Building(2, 5), Building(5, 3), Building(4, 1)]
print(F"place_mailbox(xs) = {place_mailbox(xs)}")



frozenset(dict(Counter('cat')).items())
