from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    brackets = { '(': ')', '{': '}', '[': ']' }
    stack = []
    for x in s:
        if stack and stack[-1] in brackets and brackets[stack[-1]] == x:
            stack.pop()
        else:
            stack.append(x)

    return not stack



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
