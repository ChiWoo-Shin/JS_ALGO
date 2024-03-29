N = int(input())
dp = [0] * (N+1)
def solution(n):
    if n <= 2:
        return n
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    return dp[n]

print(solution(N))