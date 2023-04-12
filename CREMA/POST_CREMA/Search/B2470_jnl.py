import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

def binarySearch():
    minAbs = [2000000000, 0, 0]
    s = 0
    e = N-1
    while s < e and e < N:
        mid = arr[s] + arr[e]
        if minAbs[0] > abs(mid):
            minAbs = [abs(mid), arr[s], arr[e]]
        if mid == 0:
            break
        elif mid > 0:
            e -= 1
        else:
            s += 1
    return minAbs[1:]


def solution():
    arr.sort()
    if arr[0] >= 0:
        return arr[:2]
    elif arr[-1] <= 0:
        return arr[-2:]
    return binarySearch()

print(*solution())