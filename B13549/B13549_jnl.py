import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split(' '))
visited = [0] * 100001
dx = [2, -1, 1]

def bfs():
    q = deque()
    q.append([start, 0])
    visited[start] = 1

    while q:
        x, t = q.popleft()
        if x == end:
            return t
    
        for i in range(3):
            if i == 0:
                nx = x * dx[i]

                if 0<=nx<100001 and not visited[nx]:
                    q.append([nx, t])
            else:
                nx = x+dx[i]
                
                if 0<=nx<100001 and not visited[nx]:
                    q.append([nx, t+1])
                    visited[nx] = 1
    
print(bfs())