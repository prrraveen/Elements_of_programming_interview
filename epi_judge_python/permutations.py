from typing import List
from test_framework import generic_test, test_utils

def gen_perms(A):
    def get_perms_helper(A, partial_result=[]):
        if not A:
            # result.append(''.join(partial_result))
            result.append(partial_result)
        for i in range(len(A)):
            get_perms_helper(A[:i] + A[i+1:], partial_result + [A[i]])
    result = []
    get_perms_helper(A)
    return result


def permutations(A: List[int]) -> List[List[int]]:
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(i, len(A)):
            print(F"A[i], A[j] = {A[i], A[j]}")
            A[i], A[j] = A[j], A[i]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result

# print(F"permutations('A') = {permutations(['A', 'B'])}")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
