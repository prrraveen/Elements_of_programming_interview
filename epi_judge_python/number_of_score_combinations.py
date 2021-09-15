from typing import List

from test_framework import generic_test

# def num_combinations_for_final_score(final_score: int, individual_play_scores: List[int]) -> int:
#     def count(S, n):
#         if n == 0:
#             return 1
#
#         if n < 0:
#             return 0
#
#         if not S and n > 0:
#             return 0
#
#         return count(S[1:], n) + count(S, n - S[0])
#
#     return count(sorted(individual_play_scores), final_score)


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    def count(S, n):
        ways = [0] * (n + 1)
        ways[0] = 1

        for i in  range(len(S)):
            for j in range(len(ways)):
                if S[i] <= j:
                    ways[j] += ways[j - S[i]]
        print(ways)
        return ways[n]

    return count(individual_play_scores, final_score)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
