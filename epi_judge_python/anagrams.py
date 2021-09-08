import collections
from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    result = {}
    for word in dictionary:
        sorted_w = ''.join(sorted(word))
        if sorted_w not in result:
            result[sorted_w] = [word]
        else:
            result[sorted_w].append(word)
    return [xs for xs in result.values() if len(xs) > 1]

# xs = ["debit card", "bad credit", "the morse code", "here come dots", "the eyes", "they see", "THL"]
#
# print(find_anagrams(xs))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
