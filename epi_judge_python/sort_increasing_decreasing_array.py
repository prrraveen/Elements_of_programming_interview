from typing import List

from test_framework import generic_test
from sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    if not A:
        return []
    def build_buckets(A):
        buckets, current_xs, increasing = [], [A[0]], True
        for i in range(1, len(A)):
            if increasing:
                if A[i] >= current_xs[-1]:
                    current_xs.append(A[i])
                else:
                    buckets.append(current_xs)
                    current_xs, increasing = [A[i]], False
            else:
                if A[i] <= current_xs[-1]:
                    current_xs.append(A[i])
                else:
                    buckets.append(current_xs[::-1])
                    current_xs, increasing = [A[i]], True

        buckets += [current_xs] if increasing else [current_xs[::-1]]
        return buckets

    buckets = build_buckets(A)
    return merge_sorted_arrays(buckets)


    # print(F"buckets = {buckets}")

# xs = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
# output = sort_k_increasing_decreasing_array(xs)
# expected = [57, 131, 190, 221, 294, 339, 418, 442, 452, 493]

# print(F"expected == output = {expected == output}")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
