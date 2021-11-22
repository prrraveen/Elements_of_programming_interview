from typing import List
import typing
import bintrees as bintrees

from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]) -> int:
    min_distance_so_far = float('inf')
    iters = bintrees.RBTree()
    for idx, sorted_arrays in enumerate(sorted_arrays):
        it = iter(sorted_arrays)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance_so_far = min(min_distance_so_far, max_value - min_value)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return min_distance_so_far
        iters.insert((next_min, min_idx), it)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
