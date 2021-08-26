from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    memo = [[0] * (len(individual_play_scores) + 1) for _ in range(final_score + 1)]

    def ways(target, avc):
        if target == 0:
            return 1
        if target < 0:
            return 0

        if avc <= 0 and target >= 1:
            return 0

        if memo[target][avc]:
            return memo[target][avc]

        result = ways(target, avc - 1) + ways(target - individual_play_scores[avc - 1], avc)
        memo[target][avc] = result
        return result

    res = ways(final_score, len(individual_play_scores))
    print(memo)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
