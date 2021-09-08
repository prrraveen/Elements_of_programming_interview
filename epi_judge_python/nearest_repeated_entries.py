import collections
import math
from typing import List

from test_framework import generic_test

def find_nearest_repetition(paragraph: List[str]) -> int:
    """did it on my own"""
    word_dict = {}
    min_dist = math.inf
    for i, word in enumerate(paragraph):
        if word not in word_dict:
            word_dict[word] = i
        else:
            min_dist = min(min_dist, i - word_dict[word])
            word_dict[word] = i
    if min_dist != math.inf:
        return min_dist
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
