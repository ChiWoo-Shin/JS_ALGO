import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

result = set()
def dfs(visited, curStep, temp, start):
    global result
    if curStep == M:
        temp.sort()
        result.add(tuple(temp))
        return 
    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, curStep+1, temp+[i], i+1)
            visited[i] = 0


def solution():
    global result
    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(visited, 0, [], i)
    arr = list(result)
    arr.sort()
    for elem in arr:
        print(*elem)

solution()