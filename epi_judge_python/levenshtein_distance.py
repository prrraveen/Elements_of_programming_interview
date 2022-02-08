from test_framework import generic_test
from main import levenshtein

def levenshtein(A: str, B: str) -> int:
    Alen = len(A)
    Blen = len(B)
    matrix = [[-1] * (Alen + 1) for _ in range(Blen + 1)]
    matrix[0][0] = 0
    for x in range(1, Blen+1):
        matrix[x][0] = matrix[x-1][0] + 1

    for y in range(1, Alen+1):
        matrix[0][y] = matrix[0][y-1] + 1

    for x in range(1, Blen + 1):
        for y in range(1, Alen + 1):
            matrix[x][y] = min(
                matrix[x-1][y] + 1,
                matrix[x][y-1] + 1,
                matrix[x-1][y-1] + (0 if A[y - 1] == B[x - 1] else 1))
    return matrix[Blen][Alen]

def levenshtein_distance(A: str, B: str) -> int:
    return levenshtein(A, B)
    # def f(a_idx, b_idx):
    #     if a_idx < 0:
    #         return b_idx + 1
    #     elif b_idx < 0:
    #         return a_idx + 1
    #     if cache[a_idx][b_idx] == -1:
    #         if A[a_idx] == B[b_idx]:
    #             cache[a_idx][b_idx] = f(a_idx - 1, b_idx - 1)
    #         else:
    #             cache[a_idx][b_idx] = 1 + min(
    #                 f(a_idx, b_idx - 1),
    #                 f(a_idx - 1, b_idx),
    #                 f(a_idx - 1, b_idx - 1))
    #     return cache[a_idx][b_idx]
    #
    # cache = [[-1] * len(B) for _ in range(len(A))]
    # return f(len(A) - 1, len(B) - 1)

A =  "GCTACACGCAGTTGCCTCGAGGAAACAAGCGCAATCGGATCGCGCATCCACACCACGACCCTGTAA"
B =  "GGGGATTCGGCATGGCGTAGGGGAATTGCTGAACGACACTCGTGCATTTAAGGGGGAACTATTACAG"
print(F"levenshtein_distance(A, B) = {levenshtein_distance(A, B)}")

# def levenshtein_distance(A: str, B: str) -> int:
#     def compute_distance_between_prefixes(A_idx, B_idx):
#         if A_idx < 0:
#             return B_idx + 1
#         elif B_idx < 0:
#             return A_idx + 1
#         if distance_between_prefixes[A_idx][B_idx]  == -1:
#             if A[A_idx] == B[B_idx]:
#                 distance_between_prefixes[A_idx][B_idx] = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
#             else:
#                 substitue_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
#                 add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
#                 delete_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
#                 distance_between_prefixes[A_idx][B_idx] = 1 + min(
#                     substitue_last, add_last, delete_last
#                 )
#         return distance_between_prefixes[A_idx][B_idx]
#
#     distance_between_prefixes = [[-1] * len(B) for _ in A]
#     return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
