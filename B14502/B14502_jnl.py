import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split(' '))))
zero_arr = []
two_arr = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero_arr.append((i, j))
        elif matrix[i][j] == 2:
            two_arr.append((i, j))
Z = len(zero_arr)

combi = set()
def dfs(visited, curStep, temp, start):
    if curStep == 3:
        combi.add(tuple(temp))
        return

    for i in range(start, Z):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, curStep+1, temp+[i], i+1)
            visited[i] = 0

def spread_virus(a, b, c):
    a_y, a_x = zero_arr[a]
    b_y, b_x = zero_arr[b]
    c_y, c_x = zero_arr[c]
    
    matrix[a_y][a_x] = 1
    matrix[b_y][b_x] = 1
    matrix[c_y][c_x] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(two_arr)

    zero_to_two = 0
    while queue:
        v_y, v_x  = queue.popleft()
        if matrix[v_y][v_x] == 0:
            zero_to_two += 1
            matrix[v_y][v_x] = 2
        for i in range(4):
            ny = dy[i] + v_y
            nx = dx[i] + v_x
            if 0<=ny<N and 0<=nx<M and matrix[ny][nx] == 0:
                queue.append((ny, nx))
    
    return zero_to_two

def reset_matrix():
    for (y, x) in zero_arr:
        matrix[y][x] = 0
    

def solution():
    #조합 구하기
    visited = [0] * Z
    dfs(visited, 0, [], 0)

    answer = N*M
    for (z1, z2, z3) in combi:
        not_safe = spread_virus(z1, z2, z3)

        answer = min(answer, not_safe)
        if answer == 0:
            break
        reset_matrix()
    
    return Z - (answer+3)

print(solution())