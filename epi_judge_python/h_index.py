from typing import List

from test_framework import generic_test


def h_index(citations):
    citations.sort(reverse=True)
    for h in reversed(range(len(citations))):
        if citations[h] >= h + 1:
            return h + 1
    return 0


xs = [9, 7, 6, 2, 1]
print(F"h_index(xs) = {h_index(xs)}")



if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
