import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, xs: List[str]) -> int:
    return 0



xs: List[str] = ['a', 'c', 'f', 'b', 'g', 'f', 'a']
# xs: List[str] = ['a', 'c', 'f', 'g', 'f', 'a']
k = len(xs)
replace_and_remove(k, xs)
print(F"Xs = {xs}")


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
