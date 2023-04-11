import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
items = []
dp = [[0] * (K+1) for _ in range(N)]
for _ in range(N):
    items.append(list(map(int, input().split(' '))))

for k in range(K+1):
    if items[0][0] <= k:
        dp[0][k] = items[0][1]

for n in range(1, N):
    w, v = items[n]
    for k in range(1, K+1):
        if w > k:
            dp[n][k] = dp[n-1][k]
        else:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-w] + v)

print(dp[N-1][K])