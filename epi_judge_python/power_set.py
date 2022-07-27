import collections
from typing import List
from test_framework import generic_test, test_utils
import copy

def generate_power_set(A):
    result = [set({})]
    for x in A:
        new_result = copy.deepcopy(result)
        [SET.add(x) for SET in new_result if x not in SET]
        print(F"new_result = {new_result}")
        result += new_result
        # result new_result)
    return result

xs = [1,2,3]
print(F"generate_power_set(xs) = {generate_power_set(xs)}")


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('power_set.py', 'power_set.tsv',
#                                        generate_power_set,
#                                        test_utils.unordered_compare))
