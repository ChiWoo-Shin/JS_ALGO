import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))
rev_arr = list(reversed(arr))
def solution():
    asc_dp = [0 for _ in range(N)]
    des_dp = [0 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                asc_dp[i] = max(asc_dp[i], asc_dp[j]+1)
            if rev_arr[j] <  rev_arr[i]:
                des_dp[i] = max(des_dp[i], des_dp[j]+1)
    
    maxLength = 0
    for i in range(N):
        l = asc_dp[i] + des_dp[-(i+1)] + 1
        maxLength = max(maxLength, l)
    return maxLength
print(solution())