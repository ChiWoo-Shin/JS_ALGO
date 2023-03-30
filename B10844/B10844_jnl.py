N = int(input())

# dp[i][j] = j로끝나는 i자릿수의 개수
dp= [[0 for _ in range(10)]for _ in range(N+1)]
def solution(n):
    if n == 1:
        return 9
    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    return sum(dp[n]) % 1000000000
print(solution(N))
