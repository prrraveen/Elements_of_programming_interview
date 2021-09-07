from typing import List

from test_framework import generic_test
import bisect


def search_first_of_k(arr: List[int], key: int) -> int:
    # if the array is empty of the element doesn't exist in the list return
    if arr and arr[0] <=  key <= arr[-1] and arr[bisect.bisect_left(arr, key)] == key:
        return bisect.bisect_left(arr, key)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))