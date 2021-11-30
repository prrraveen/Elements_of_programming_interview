from typing import List
from test_framework import generic_test


# def apply_permutation(perm: List[int], A: List[int]) -> None:
#     result = [None] * len(perm)
#     for i, x in enumerate(perm):
#         result[x] = A[i]
#     A[:] = result
#     return result

def apply_permutation(perm: List[int], A: List[int]) -> None:
    for j in range(len(A)):
        i = perm[j]
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            # perm[i], perm[perm[i]] = perm[perm[i]], perm[i]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return A

# def apply_permutation(perm: List[int], A: List[int]) -> None:
#     i  = 0
#     for i in range(len(A)):
#         while perm[i] != i:
#             A[perm[i]], A[i] = A[i], A[perm[i]]
#             perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

# def apply_permutation(perm: List[int], A: List[int]) -> None:
#     for i in range(len(A)):
#         # check if the element at index i has not been moved by checking if
#         # perm[i] is not negative.
#         next = i
#         while perm[next] >= 0:
#             A[i], A[perm[next]] = A[perm[next]], A[i]
#             temp = perm[next]
#             perm[next] -= len(perm)
#             next = temp
#         #restore perm.
#     perm[:] = [a + len(perm) for a in perm]





# xs = ['a', 'b', 'c', 'd']
# perm = [2, 0, 1, 3]
# expected = ['b', 'c', 'a', 'd']

xs = ['a', 'b', 'c', 'd', 'e', 'f']
perm = [1, 0, 2, 3, 4, 5]
# perm = [1, 5, 0, 4, 2, 3]
expected = ['c', 'a', 'e', 'f', 'd', 'b']

# perm = [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
# xs = [7, 10, 14, 1, 15, 9, 16, 4, 0, 11, 12, 18, 3, 13, 5, 8, 17, 2, 6]
# expected = [5, 9, 10, 4, 15, 13, 17, 7, 8, 0, 1, 14, 2, 6, 3, 16, 18, 11, 12]
output = apply_permutation(perm, xs)
# print(F"expect = {expected}")
print(F"output = {output}")



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
