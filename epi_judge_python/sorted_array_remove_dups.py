import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def delete_duplicates(A: List[int]) -> int:
    write_idx = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[write_idx] = A[i]
            write_idx += 1
    return write_idx

# xs = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
xs = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(xs)
print(F"delete_duplicates(xs) = {delete_duplicates(xs)}")
print(xs)

# # Returns the number of valid entries after deletion.
# def delete_duplicates(A: List[int]) -> int:
#     if not A:
#         return 0
#     write_index = 1
#     for i in range(1, len(A)):
#         if A[write_index - 1] != A[i]:
#             A[write_index] = A[i]
#             write_index += 1
#     return write_index




@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
