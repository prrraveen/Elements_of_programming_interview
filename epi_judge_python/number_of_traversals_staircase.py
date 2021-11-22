from test_framework import generic_test

# def number_of_ways_to_top(n: int, k: int) -> int:
#     def f(n):
#         if n < 0:
#             return 0
#         if ways[n] != -1:
#             return ways[n]
#         ways[n] = sum([f(n - i) for i in range(1, k+1)])
#
#         return ways[n]
#
#     if k == 0 or n == 0:
#         return 0
#     ways = [-1] * (n + 1)
#     ways[0] = ways[1] = 1
#     # print(F"ways = {ways}")
#     return f(n)

def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    def compute_number_of_ways_to_h(h):
        if h <= 1:
            return 1
        if number_of_ways_to_h[h] == 0:
            number_of_ways_to_h[h] = sum(
                compute_number_of_ways_to_h(h - i)
                for i in range(1, min(maximum_step, h) + 1) )
        return number_of_ways_to_h[h]

    number_of_ways_to_h = [0] * (top + 1)
    return compute_number_of_ways_to_h(top)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
