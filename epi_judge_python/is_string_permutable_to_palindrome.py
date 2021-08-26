from collections import Counter

from test_framework import generic_test


def can_form_palindrome(xs: str) -> bool:
    return sum([x % 2 for x in Counter(xs).values()]) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
