import heapq
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    min_heap = [x for x in A[:k]]
    heapq.heapify(min_heap)
    for x in A[k:]:
        heapq.heappushpop(min_heap, x)

    sort_result = []
    while min_heap:
        sort_result.append(min_heap.pop())
    
    return sort_result[-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
