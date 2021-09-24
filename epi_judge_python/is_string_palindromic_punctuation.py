import string

from test_framework import generic_test

def is_palindrome(xs: str) -> bool:
    if not xs:
        return True
    tester = set(string.ascii_letters + string.digits)
    left, right = 0, len(xs) - 1
    while left < right:
        if xs[left] not in tester:
            left += 1
            continue
        if xs[right] not in tester:
            right -= 1
            continue
        if xs[left].lower() == xs[right].lower():
            left += 1
            right -= 1
        else:
            return False
    if left != right:
        return False
    return True

# def is_palindrome_v1(xs: str) -> bool:
#     tester = set(string.ascii_lowercase + string.digits)
#     ys = []
#     # print(F"Xs = {xs}")
#     for c in xs.lower():
#         if c in tester:
#             ys.append(c)
#     # print(F"Ys = {ys}")
#     mid = len(ys) // 2
#
#     for i in range(mid):
#         if ys[i] != ys[~i]:
#             return False
#     return True




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
