from typing import List

from test_framework import generic_test

# def num_combination_for_final_score(score: int, point_plays: [int]) -> int:
#     def f(remaining, partial_result):
#         if remaining == 0:
#             # print(F"remaining, partial_result = {remaining, partial_result}")
#             score_collector.add(tuple(sorted(partial_result)))
#             return
#         elif remaining < 0:
#             return
#         for point_play in point_plays:
#             f(remaining - point_play, partial_result + [point_play])
#     score_collector = set()
#     f(score, [])
#     # print(F"score_collector = {score_collector}")
#     return len(score_collector)


def num_combinations_for_final_score(final_score: int, individual_play_score: [int]) -> int:
    num_combinations_for_score = [[1] + [0] * final_score for _ in range(2)]

    for i in range(len(individual_play_score)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[0][j]
                                 if i >= 1 else 0)
            with_this_play = (
                num_combinations_for_score[1][j - individual_play_score[i]]
                if j >= individual_play_score[i] else 0
            )
            num_combinations_for_score[1][j] = (
                    without_this_play + with_this_play
            )
        num_combinations_for_score[0] = num_combinations_for_score[1]
        num_combinations_for_score[1] = [1] + [0] * final_score
    return num_combinations_for_score[0][-1]

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


# def num_combinations_for_final_score(final_score: int,
#                                      individual_play_scores: List[int]) -> int:
#     return _test(final_score, individual_play_scores)
#     def count(S, n):
#         ways = [0] * (n + 1)
#         ways[0] = 1
#
#         for i in  range(len(S)):
#             for j in range(len(ways)):
#                 if S[i] <= j:
#                     ways[j] += ways[j - S[i]]
#         print(ways)
#         return ways[n]
#
#     return count(individual_play_scores, final_score)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
