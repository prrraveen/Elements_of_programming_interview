from typing import List

from test_framework import generic_test


# def longest_subarray_with_distinct_entries(A):
#     result, n  = 0, len(A)
#     for i in range(n):
#         ys = set()
#         for j in range(i,n):
#             if A[j] in ys:
#                 result = max(result, len(ys))
#                 break
#             else:
#                 ys.add(A[j])
#             result = max(result, len(ys))
#     return result

# def longest_subarray_with_distinct_entries(A):
#     result, n  = 0, len(A)
#     left = 0
#     while left < n:
#         right, ys = left, {}
#         while right < n:
#             elem = A[right]
#             if elem not in ys:
#                 ys[elem] = right
#                 right += 1
#             else:
#                 result = max(result, len(ys))
#                 left = ys[elem]
#                 break
#         result = max(result, len(ys))
#         left += 1
#     return result

def longest_subarray_with_distinct_entries(A):
    most_recent_occurrence = {}
    longest_dup_free_subarray_start_idx = result = 0

    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i
    return max(result, len(A) - longest_dup_free_subarray_start_idx)

# def longest_subarray_with_distinct_entries(A):
#     result, n  = 0, len(A)
#     left = 0
#     while left < n:
#         right, ys = left, {}
#         while right < n:
#             elem = A[right]
#             if elem not in ys:
#                 ys[elem] = right
#                 right += 1
#             else:
#                 result = max(result, len(ys))
#                 left = ys[elem]
#                 break
#         result = max(result, len(ys))
#         left += 1
#     return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
