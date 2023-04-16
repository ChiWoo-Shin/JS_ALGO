import sys
input = sys.stdin.readline

R, C = map(int, input().split(' '))
matrix = []
for _ in range(R):
    matrix.append(list(input().rstrip()))
maxLength = 0

def dfs(visited, y, x, temp):
    global maxLength
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maxLength = max(maxLength, temp)

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if 0<=ny<R and 0<=nx<C and not visited[ord(matrix[ny][nx])-65]:
            visited[ord(matrix[ny][nx])-65] = 1
            dfs(visited, ny, nx, temp+1)
            visited[ord(matrix[ny][nx])-65]  = 0
    
    

def solution():
    visited = [0] * 26
    visited[ord(matrix[0][0])-65] = 1
    dfs(visited, 0,0,1)
    return maxLength
    

print(solution())