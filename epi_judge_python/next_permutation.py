from typing import List

from test_framework import generic_test

def next_permutation(A: List[int]) -> List[int]:
    k = len(A) - 2
    while k >= 0 and A[k] >= A[k+1]:
        k -= 1

    if k == -1:
        return []

    l = k

    for i in reversed(range(k+1, len(A))):
        if A[i] > A[k]:
            l = i
            break

    A[k], A[l] = A[l], A[k]

    A[:] = A[:k+1] + A[k+1:][::-1]
    return A

# def next_permutation(perm ):
#     # find the first entry from the right that is smaller than the entry
#     # immediately after it.
#     inversion_point = len(perm) - 2
#     while (inversion_point >= 0
#            and perm[inversion_point] >= perm[inversion_point + 1]):
#         inversion_point -= 1
#
#     print(F"inversion_point, A[inversion_point], A[inversion_point + 1] = {inversion_point, A[inversion_point], A[inversion_point + 1]}")
#     if inversion_point == -1:
#         return []  # perm is the last permutation.
#
#     # swap the smallest entry after index inversion_point that is greater than
#     # perm[inversion_point]. since entries in perm are decreasing after
#     # inversion_point, if we search in reverse order, the first entry that is
#     # greater than perm[inversion_point] is the entry to swap with.
#     for i in reversed(range(inversion_point + 1, len(perm))):
#         if perm[i] > perm[inversion_point]:
#             perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
#             break
#
#     # entries in perm must appear in decreasing order after inversion_point,
#     # so we simply reverse these entries to get the smallest dictionary order.
#     perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
#     return perm

A = [8, 6, 15, 18, 17, 10, 17, 13, 16, 1, 6, 1, 18, 11, 1, 12, 15, 6]
expected = [8, 6, 15, 18, 17, 10, 17, 13, 16, 1, 6, 1, 18, 11, 1, 15, 6, 12]
result =   [8, 6, 15, 18, 17, 10, 17, 13, 16, 1, 6, 1, 18, 11, 1, 12, 6, 15]
print(F"next_permutation(A) = {next_permutation(A)}")



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
