# 합분해

import sys
input = sys.stdin.readline
N, K = map(int, input().split(' '))
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

def solution(k, n):
    if k == 1:
        return 1
    dp[1] = [1] * (N+1)
    for i in range(2, k+1):
        for j in range(n+1):
            if j == 0:
                dp[i][j] = 1
            else:
                for l in range(j+1):
                    dp[i][j] += dp[i-1][l]
    return dp[k][n] % 1000000000

print(solution(K, N))