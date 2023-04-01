import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

start, end = map(int, input().split(' '))

def solution(start, end):
    visited = [0] * 100001
    distance = [INF] * 100001
    distance[start] = 0

    dx = [2, -1, 1]

    heap = [[0, start]]
    while heap:
        cnt, node = heapq.heappop(heap)
        visited[node] = 1
        if node == end:
            break
        for i in range(3):
            if i == 0:
                nx = node*dx[i]
                if nx <100001 and not visited[nx]:
                    if distance[nx] > cnt:
                        distance[nx] = cnt
                        heapq.heappush(heap, [cnt, nx])
            else:
                nx = node+dx[i]
                if 0<=nx<100001 and not visited[nx]:
                    if distance[nx] > cnt+1:
                        distance[nx] = cnt+1
                        heapq.heappush(heap, [cnt+1,nx])
    
    return distance[end]
            
print(solution(start, end))