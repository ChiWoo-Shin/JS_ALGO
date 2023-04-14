import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort()

def solution():
    dp = [0] * (K+1)
    
    for i in range(N):
        coin = coins[i]
        if coin > K:
            break
        dp[coin] += 1
        for j in range(coin, K+1):
            dp[j] += dp[j-coin]

    return dp[K]


print(solution()) 