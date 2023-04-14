import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = [0]
for _ in range(N):
    arr.append(int(input()))

def solution():
    dp = [[0] * (M+1) for _ in range(N+1)]
    arr.sort()

    for i in range(1, len(arr)):
        for j in range(1, M+1):
            if j < arr[i]:
                dp[i][j] = dp[i-1][j]
            elif j == arr[i]:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i]]
    return dp[N][M]

print(solution())
