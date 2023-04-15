import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(input().rstrip()))


def bfs(visited, start_y, start_x):
    queue = deque([[start_y, start_x]])
    color = matrix[start_y][start_x]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and matrix[ny][nx] == color:
                queue.append([ny, nx])
                visited[ny][nx] = 1

def bbfs(visited, start_y, start_x):
    queue = deque([[start_y, start_x]])
    color = matrix[start_y][start_x]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                if (color == 'R' or color == 'G') and (matrix[ny][nx] == 'R' or  matrix[ny][nx] == 'G'):
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
                elif color == 'B' and matrix[ny][nx] == 'B':
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
                    

def solution():
    visited = [[0] * N for _ in range(N)]
    R, G, B = 0, 0, 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                if matrix[i][j] == 'R': R+=1
                elif matrix[i][j] == 'G': G+=1
                else: B+=1
                bfs(visited, i, j)
    
    visited1 = [[0] * N for _ in range(N)]
    RG_, B_ = 0, 0
    for i in range(N):
        for j in range(N):
            if not visited1[i][j]:
                visited1[i][j] = 1
                if matrix[i][j] == 'R' or  matrix[i][j] == 'G': RG_ += 1
                else: B_+=1
                bbfs(visited1, i, j)

    
    return [R+G+B, RG_+B_]

print(*solution())