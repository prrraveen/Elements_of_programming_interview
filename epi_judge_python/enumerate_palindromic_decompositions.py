from typing import List
from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(text):
            result.append(partial_partition.copy())
            return

        for i in range(offset + 1, len(text) + 1):
            prefix = text[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(
                    i, partial_partition + [prefix])

    result: List[List[str]] = []
    directed_palindrome_decompositions(offset=0, partial_partition=[])
    return result

# def palindrome_decompositions(text: str) -> List[List[str]]:
#     print(F"text = {text}")
#     def palindrome_decompositions_helper(size, index, partial_result=[]):
#         if index >= len(text):
#             if len(''.join(partial_result)) == len(text) and partial_result not in result:
#                     result.append(partial_result)
#             return
#
#         substr = text[index:index+size]
#         if substr == substr[::-1]:
#             palindrome_decompositions_helper(size, index + size, partial_result + [substr])
#
#         palindrome_decompositions_helper(size, index + 1, partial_result + [text[index]])
#     result = []
#     for size in range(len(text)):
#         palindrome_decompositions_helper(size + 1, 0)
#     return result

# xs = "aba"
# print(F"palindrome_decompositions(xs) = {palindrome_decompositions(xs)}")

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
