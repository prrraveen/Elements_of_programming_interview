from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    if len(s) == 0:
        return 0

    T = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    result = 0
    for i in range(len(s)):
        ch = s[i]
        result += T[ch]
        if i != 0:
            if (ch == 'X' or ch == 'V') and s[i - 1] == 'I':
                result -= 2

            if (ch == 'L' or ch == 'C') and s[i - 1] == 'X':
                result -= 20

            if (ch == 'D' or ch == 'M') and s[i - 1] == 'C':
                result -= 200

    return result




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))


# print(F"roman_to_integer('III') = {roman_to_integer('CD')}")