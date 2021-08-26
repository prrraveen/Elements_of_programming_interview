from typing import List

from test_framework import generic_test
import bisect


def search_first_of_k(arr: List[int], key: int) -> int:
    result = bisect.bisect_left(arr, key)
    if result == len(arr):
        return -1
    if arr[result] != key:
        return -1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',

jfdFD
                                       jfdFD
    jfdFD
    jfdFD
    jfdFD
    jfdFD
    jfdFD