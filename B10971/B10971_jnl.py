import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for  _ in range(N):
    matrix.append(list(map(int, input().split(' '))))

minCost = sys.maxsize

def dfs(visited, curStep, temp, start, origin):
    global minCost
    if curStep == N:
        if matrix[start][origin] != 0:
            temp += matrix[start][origin]
            minCost = min(minCost, temp)
        return
    
    if temp >= minCost:
        return

    
    for i in range(N):
        if not visited[i] and matrix[start][i] != 0:
            visited[i] = 1
            dfs(visited, curStep+1, temp+matrix[start][i], i, origin)
            visited[i] = 0


def solution():
    global minCost
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        dfs(visited, 1, 0, i, i)
    return minCost

print(solution())

