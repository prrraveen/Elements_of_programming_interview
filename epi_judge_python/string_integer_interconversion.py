from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x) -> str:
    result = []
    is_negative = False

    if x < 0:
        x, is_negative = -x, True

    while True:
        result.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break


    return ('-' if is_negative else  '') + ''.join(reversed(result))




def string_to_int(s: str) -> int:
    is_negative = False
    result = 0

    m = 1
    for c in reversed(s):
        if c == '-':
            is_negative = True
            continue
        if c == '+':
            continue
        temp = (ord(c) - ord('0')) * m
        result += temp
        m *= 10
    return -result if is_negative else result



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
