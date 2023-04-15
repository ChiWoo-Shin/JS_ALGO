import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

asc_arr = [1 for _ in range(N)]
des_arr = [1 for _ in range(N)]


def solution():
    rev = list(reversed(arr))
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                asc_arr[i] = max(asc_arr[i], asc_arr[j]+1)
    
            if rev[i] > rev[j]:
                des_arr[i] = max(des_arr[i], des_arr[j]+1)
                
    maxLength = 0
    for i in range(N):
        maxLength = max(maxLength, asc_arr[i]+des_arr[-(i+1)]-1)
    return maxLength

print(solution())


