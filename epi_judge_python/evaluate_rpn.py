import operator
from functools import reduce
from typing import List

from test_framework import generic_test



def evaluate(expression: str) -> int:
    intermediate_result = []
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in expression.split(','):
        if token in OPERATORS:
            intermediate_result.append(OPERATORS[token](
                intermediate_result.pop(), intermediate_result.pop()
            ))
        else:
            intermediate_result.append(int(token))
    # return intermediate_result[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
