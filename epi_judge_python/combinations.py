from typing import List
from test_framework import generic_test, test_utils
from power_set import generate_power_set

# def combinations(n: int, k: int) -> List[List[int]]:
#     xs = list(range(1, n + 1))
#     power_set_xs = generate_power_set(xs)
#     return [x for x in power_set_xs if len(x) == k]

def combinations(n: int, k: int) -> List[List[int]]:
    def directed_combination(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return

        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:

    result = []
    directed_combination(1, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
