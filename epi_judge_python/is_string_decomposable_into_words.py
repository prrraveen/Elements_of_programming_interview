import functools
from typing import List, Set
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i+1] in dictionary:
            last_length[i] = i + 1

        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j+1:i+1] in dictionary:
                    last_length[i] = i - j
                    break
    decompositions = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx+1 - last_length[idx]:idx+1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    return decompositions

# def decompose_into_dictionary_words(domain: str,
#                                     dictionary: Set[str]) -> List[str]:
#     def decompose(index, partial_result=[]):
#         # print(F"index = {index}")
#         # print(F"partial_result = {partial_result}")
#         if index == len(domain):
#             decompositions.append(partial_result)
#
#         for word in dictionary:
#             if domain.startswith(word, index):
#                 # print(F"word = {word}")
#                 decompose(index + len(word), partial_result + [word])
#
#     decompositions = []
#     decompose(0)
#     if decompositions:
#         return decompositions[0]
#     return decompositions


# domain = 'szzohzqh'
# dictionary = {'szzoh', 'szz', 'oh', 'zqh'}
# decompositions = ['szzoh', 'zqh']
# # name = "AMANAPLANACANAL"
# # dictn = {'A', 'MAN', 'PLAN', 'CANAL'}
# name = "asseafseaefseefaaffffefafafefe"
#
# dictn= ["af", "afaa", "ss", "efaa", "sfsss", "eas", "sesae", "ses", "efe", "a", "sfef", "fafse", "aae", "fs",
#              "fea", "easa", "ee", "asef", "fafa", "aaa", "f", "eeaee", "aea", "efs", "eafs", "se", "ase", "easf", "ae",
#              "eaef", "afe", "aass", "ffef", "sesef", "ffea", "ass", "sea", "eeas", "fa", "saf", "sasf", "sa", "eesf",
#              "eee", "aa", "sas", "ff", "sfeff", "fse", "e"]


# output = decompose_into_dictionary_words(domain, dictionary)
# for o in output:
#     print(F"o = {o}")

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
