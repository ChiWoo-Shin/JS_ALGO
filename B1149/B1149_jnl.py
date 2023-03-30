import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    [R, G, B] = list(map(int, input().split(' ')))
    if (i == 0):
        dp[i] = [R, G, B]
    else:
        dp[i][0] = R + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = G + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = B + min(dp[i-1][0],dp[i-1][1])

print(min(dp[N-1]))

    
