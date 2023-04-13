import sys
from itertools import combinations

input = sys.stdin.readline
MAP = []
INF = float('inf')
N, M = map(int, input().split(' '))
for _ in range(N):
    MAP.append(list(map(int, input().split(' '))))

result = set()
def dfs(visited, curStep, temp, start):
    global result
    if curStep == M:
        temp.sort()
        result.add(tuple(temp))
        return

    for i in range(start, len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(visited, curStep+1, temp+[i], start+1)
            visited[i] = 0

def solution():
    chickenPos = []
    homePos = []
    minSum = float('inf')
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                chickenPos.append([i, j])
            elif MAP[i][j] == 1:
                homePos.append([i, j])
    
    for i in range(len(chickenPos)):
        visited = [0] * len(chickenPos)
        dfs(visited, 0, [], i)

    for subArr in result:
        temp = 0
        for [hy, hx] in homePos:
            chi_dist = INF
            for i in range(M):
                cy, cx = chickenPos[subArr[i]]
                chi_dist = min(chi_dist, abs(hy-cy)+abs(hx-cx))
            temp += chi_dist
            
        minSum = min(minSum, temp)
    return minSum

print(solution())