import collections
import itertools
from typing import List
from test_framework import generic_test

# def get_substring_start_idx(s, substring):
#     result, i, n = [], 0, len(substring)
#     while i < len(s):
#         if (s[i] == substring[0]
#                 and i + n <= len(s)
#                 and s[i:i+n] == substring):
#             result.append(i)
#         i += 1
#
#     return result

# s = "eddvuieddvui"
# substring = 'eddvui'
# print(F"get_substring_start_idx(s, substring) = {get_substring_start_idx(s, substring)}")
# print(F"get_substring_start_idx('') = {get_substring_start_idx('barfoobarthefoobarmands', 'foobar')}")

# def find_all_substrings(s: str, words: List[str]) -> List[int]:
#     perms = list(map(''.join, list(itertools.permutations(words))))
#     # print(F"perms = {perms}")
#     result = []
#     for substring in perms:
#         result += get_substring_start_idx(s, substring)
#     return sorted(list(set(result)))


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be possible
                return False
        return True
    word_to_freq = collections.Counter(words)
    unit_size = len(words[0])
    xs = [
        i for i in range(len(s) - unit_size * len(words) + 1)
        if match_all_words_in_dict(i)
    ]
    return xs


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
