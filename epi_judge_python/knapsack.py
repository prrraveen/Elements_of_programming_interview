import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from main import  knapsack, weight, xs

Item = collections.namedtuple('Item', ('weight', 'value'))



def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    return knapsack(items, capacity)
    def optimum_subject_to_item_capacity(k, available_capacity):
        if k < 0:
            return 0
        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_capacity(k-1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight else (
                items[k].value + optimum_subject_to_item_capacity(k-1, available_capacity - items[k].weight)
            ))
            V[k][available_capacity] = max(without_curr_item, with_curr_item)
        return V[k][available_capacity]

    V  = [[-1] * (capacity + 1) for _ in items]
    return optimum_subject_to_item_capacity(len(items) - 1, capacity)

# print(F"optimum_subject_to_capacity(xs, weight) = {optimum_subject_to_capacity(xs, weight)}")

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))

# def knapsack(items: [Item], capacity):
#     def optimum_subject_to_item_capacity(k: int, available_capacity: int) -> int:
#         if k < 0:
#             return 0
#         if V[k][available_capacity] == -1:
#             v, w = items[k]
#             without_this_weight = optimum_subject_to_item_capacity(k - 1, available_capacity)
#             with_this_item = (0 if available_capacity < w else (
#                     v + optimum_subject_to_item_capacity(k-1, available_capacity - w)
#             ))
#             V[k][available_capacity] = max(with_this_item, without_this_weight)
#         return V[k][available_capacity]
#     V = [[-1] * (capacity + 1) for _ in items]
#     return optimum_subject_to_item_capacity(len(items) - 1, capacity)
