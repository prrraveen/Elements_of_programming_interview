import math
from typing import List

from test_framework import generic_test, test_utils


# def generate_balanced_parentheses(num_pairs: int) -> List[str]:
#     def _generate_balanced_parentheses(num_of_left_parens_needed,
#                                        num_of_right_parens_needed,
#                                        valid_prefix,
#                                        result=[]):
#         if num_of_right_parens_needed > 0:
#             _generate_balanced_parentheses(num_of_left_parens_needed - 1,
#                                            num_of_right_parens_needed,
#                                            valid_prefix + '(')
#         if num_of_left_parens_needed < num_of_right_parens_needed:
#             _generate_balanced_parentheses(num_of_left_parens_needed,
#                                            num_of_right_parens_needed - 1,
#                                            valid_prefix + ')')
#         if not num_of_right_parens_needed:
#             result.append(valid_prefix)
#         return result
#     return _generate_balanced_parentheses(num_pairs, num_pairs, valid_prefix='')

def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    if num_pairs == 0:
        return ['']
    result = {'()'}
    for _ in range(1,num_pairs):
        new_result = set()
        for item in result:
            new_result.add(F"(){item}")
            new_result.add(F"({item})")
            new_result.add(F"{item}()")
        result = new_result
    return list(result)



# def generate_balanced_parentheses(num_pairs: int) -> List[str]:
#     def directed_generate_balanced_parentheses(num_left_parens_needed,
#                                                num_right_parens_needed,
#                                                valid_prefix,
#                                                result=[]):
#         if num_left_parens_needed > 0:  # Able to insert '('.
#             directed_generate_balanced_parentheses(num_left_parens_needed - 1,
#                                                    num_right_parens_needed,
#                                                    valid_prefix + '(')
#         if num_left_parens_needed < num_right_parens_needed:
#             # Able to insert ')'.
#             directed_generate_balanced_parentheses(num_left_parens_needed,
#                                                    num_right_parens_needed - 1,
#                                                    valid_prefix + ')')
#         if not num_right_parens_needed:
#             result.append(valid_prefix)
#         return result
#
#     return directed_generate_balanced_parentheses(num_pairs,
#                                                   num_pairs,
#                                                   valid_prefix='')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
