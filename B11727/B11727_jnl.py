import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
    return dp[n]

print(solution(N))