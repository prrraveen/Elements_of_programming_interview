def solution(N, K):
    glass_count = 0
    N = min(N, K)
    while N > 0 and K > 0:
        if K >= N:
            K = K - N
            N -= 1
            glass_count += 1
        else:
            N -= 1

    if K > 0:
        return -1
    return glass_count


print(F"solution(5, 8) = {solution(5, 8)}") #2
print(F"solution(4, 10) = {solution(4, 10)}")
print(F"solution(1, 2) = {solution(1, 2)}") #4
print(F"solution(10, 5) = {solution(10, 5)}") #4
print(F"solution(20, 100) = {solution(20, 100)}") #4
print(F"solution(100, 20) = {solution(20, 100)}") #4
