import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

def solution():
    dp = [0] * N
    dp[0] = arr[0] 
    for i in range(1, N):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+arr[i])
    return max(dp)

print(solution())