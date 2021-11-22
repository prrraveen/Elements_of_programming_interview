import collections
from typing import List
from test_framework import generic_test

# def can_reach_end(A: List[int]) -> bool:
#     q = collections.deque([0])
#     while q:
#         index = q.popleft()
#         for i in range(index + 1, index + A[index] + 1):
#             if i >= len(A) - 1:
#                 return True
#             else:
#                 q.append(i)
#             # print(F"i, A[i] = {i, A[i]}")
#         pass
#
#     return False

# def can_reach_end(A: List[int]) -> bool:
#     reach_to = len(A) - 1
#     i = reach_to - 1
#     while i >= 0:
#         if i + A[i] >= reach_to:
#             reach_to = i
#         i -= 1
#     if reach_to == 0:
#         return True
#     return False


def can_reach_end(A: List[int]) -> bool:
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    steps = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        if A[i] + i > furthest_reach_so_far:
            steps += 1
            furthest_reach_so_far = A[i] + i
        i += 1
    return furthest_reach_so_far >= last_index

# xs = [3, 3, 1, 0, 2, 0, 1]
# xs = [3, 2, 0,  0,  2,  0,  1]
# xs = [1, 1, 0, 0]
xs = [1, 3, 5, 8, 10, 2, 6, 7, 6, 8, 9]
xs = [2, 3, 1, 1, 4]
print(F"can_reach_end(xs) = {can_reach_end(xs)}")




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
