from collections import deque
INF = float('inf')
def bfs(R, C, maps, dp):
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<R and 0<=nx<C and maps[ny][nx] == 1 and dp[ny][nx] == INF:
                dp[ny][nx] = dp[y][x]+1
                if ny == R-1 and nx == C-1:
                    return dp[ny][nx]
                queue.append((ny, nx))
    return -1
        
        
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dp = [[INF] * m for _ in range(n)]
    
    if (n-2 >= 0 and m-2 >= 0) and (maps[n-2][m-2] == 0 and maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0):
        return -1
    
    dp[0][0] = 1
    result = bfs(n, m, maps, dp)
    return result