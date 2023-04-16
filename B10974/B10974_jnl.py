import sys
input = sys.stdin.readline

N = int(input())
result = set()
def dfs(visited, curStep, temp):
    if curStep == N:
        result.add(tuple(temp))
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, curStep+1, temp+[i])
            visited[i] = 0


def solution():
    global result
    visited = [0] * (N+1)
    dfs(visited, 0, [])

    result = list(result)
    result.sort()

    for elem in result:
        print(*elem)

solution()