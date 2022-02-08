import collections
from typing import List
from test_framework import generic_test, test_utils


# def power_set(A: [int]) -> [[int]]:
#     def f(i):
#         if i == len(A):
#             return
#         partial_result = [x + [A[i]] for x in result]
#         result.extend(partial_result)
#         f(i + 1)
#     result = [[]]
#     f(0)
#     return result

# def generate_power_set(input_set: List[int]) -> List[List[int]]:
#     def f(to_be_selected, selected_so_far):
#         if to_be_selected == len(input_set):
#             result.append(selected_so_far)
#             return
#         f(to_be_selected + 1, selected_so_far)
#         f(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])
#     result = []
#     f(0, [])
#     return result

def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def f(i, partial_result):
        if i == len(input_set):
            result.append(partial_result)
            return

        f(i + 1, partial_result + [input_set[i]])
        while i < len(input_set) - 1 and input_set[i] == input_set[i + 1]:
            i += 1
        f(i + 1, partial_result)

    input_set.sort()
    result = []
    f(0, [])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
