import functools
import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result, min_heap = [], []

    sorted_arrays_iters = [iter(xs) for xs in sorted_arrays]
    for i, it in enumerate(sorted_arrays_iters):
        first_item = next(it, None)
        if first_item is not None:
            heapq.heappush(min_heap, (first_item, i))

    while min_heap:
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap)
        smallest_entry_array = sorted_arrays_iters[smallest_entry_i]
        result.append(smallest_entry)
        next_element = next(smallest_entry_array, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_i))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
