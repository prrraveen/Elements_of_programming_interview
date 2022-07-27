from collections import Counter

from test_framework import generic_test

def sol(A):
    # print(F"len(s) = {len(s)}")
    counter = Counter(A)
    # print(F"counter = {counter}")
    odd_count = 0
    for freq in counter.values():
        # print(freq)
        if freq % 2 == 1:
            if odd_count == 0:
                odd_count += 1
            else:
                return False
    return True


def can_form_palindrome(xs: str) -> bool:
    return sol(xs)
    # return sum([x % 2 for x in Counter(xs).values()]) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
