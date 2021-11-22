from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    xs = [False, False] + [True] * (n - 1)
    for i in range(len(xs)):
        if xs[i]:
            j = 2 * i
            while j < len(xs):
                xs[j] = False
                j += i
    return [i for i in range(len(xs)) if xs[i] is True]


print(generate_primes(18))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
