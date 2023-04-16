import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

candidates = set()
def dfs(visited, curStep, temp):
    if curStep == N:
        candidates.add(tuple(temp))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, curStep+1, temp+[i])
            visited[i] = 0

def solution():
    visited = [0] * N
    dfs(visited, 0, [])

    maxSum = 0
    for candidate in candidates:
        temp = 0
        for i in range(N-1):
            temp += abs(arr[candidate[i]] - arr[candidate[i+1]])
        maxSum = max(maxSum, temp)
    return maxSum

print(solution())