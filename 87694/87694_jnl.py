from collections import deque

def bfs(matrix, curX, curY, itemX, itemY):
    queue = deque([[curY, curX]])
    
    visited = [[0] *102 for _ in range(102)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        y, x = queue.popleft()
        if y == itemY and x == itemX:
            return visited[y][x]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<102 and 0<=ny<102 and matrix[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x]+1
                queue.append([ny, nx])
                             
                             
                             
def solution(rectangle, characterX, characterY, itemX, itemY):
    matrix = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if y1<y<y2 and x1<x<x2:
                    matrix[y][x] = 0
                elif matrix[y][x] == -1:
                    matrix[y][x] = 1
                    
    result = bfs(matrix, characterX*2, characterY*2, itemX*2, itemY*2)
    return result//2     
                
            
            
    