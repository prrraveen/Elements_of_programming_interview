import functools

from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    result = 0
    d = 0
    result = functools.reduce(lambda x, ch: x * 26  + ord(ch) - ord('A') + 1, col, 0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
