# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))

def solution(n):
    dp =[[0, 0, 0] for _ in range(n)]
    dp[0] = [0, 0, wines[0]]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][2] + wines[i]
        dp[i][2] = dp[i-1][0] + wines[i]
    return max(dp[n-1])

print(solution(N))