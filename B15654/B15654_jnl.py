import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

result = set()
def dfs(visited, curDepth, temp):
    if curDepth == M:
        result.add(tuple(temp))
        return
    
    for i in range( N):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, curDepth+1, temp+[arr[i]])
            visited[i] = 0


def solution():
    global result
    visited = [0] * N
    dfs(visited, 0, [])
    result = list(result)
    result.sort()

    for elem in result:
        print(*elem)

solution()