from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    # TODO - you fill in here.
    if not s:
        return ''
    result, i, number_reading = [], 0, []
    while i < len(s):
        if s[i].isdigit():
            number_reading.append(s[i])
        else:
            result += s[i] * int(''.join(number_reading))
            number_reading = []
        i += 1
    return ''.join(result)


def encoding(s):
    # TODO - you fill in here.
    if not s:
        return ''
    last_char, count, result = s[0], 1, []
    for ch in s[1:]:
        if ch == last_char:
            count += 1
        else:
            result += [str(count), last_char]
            count = 1
            last_char = ch

    result += [str(count), last_char]
    return ''.join(result)



def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
