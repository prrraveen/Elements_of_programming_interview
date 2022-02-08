from test_framework import generic_test
from  main import ways

def number_of_ways(n: int, m: int) -> int:
    if n == m == 1:
        return 1
    first_row = [0] + [1] * (min(n, m) - 1)
    second_row = [1] + [0] * (min(n, m) - 1)
    for _ in range(max(n, m) - 1):
        for i in range(1, len(second_row)):
            second_row[i] = second_row[i - 1] + first_row[i]
        first_row = second_row
        second_row = [1] + [0] * (min(n, m) - 1)
    return first_row[-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
