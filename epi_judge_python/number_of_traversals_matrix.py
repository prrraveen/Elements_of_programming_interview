from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    cache = [[1] * m for _ in range(n)]
    cache[0][0] = 1
    for i in range(n):
        cache[i][0] = 1
    for i in range(m):
        cache[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            cache[i][j] = cache[i][j-1] + cache[i - 1][j]
    return cache[n - 1][m - 1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
