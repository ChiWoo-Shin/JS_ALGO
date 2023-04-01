import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split(' ')) 
    graph[a].append([b, c])
start, end = map(int, input().split(' '))

def dijkstra(start, end):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cost, curCity = heapq.heappop(heap)
        for [nextCity, nextCost] in graph[curCity]:
            if cost + nextCost < distance[nextCity]:
                distance[nextCity] = cost + nextCost
                heapq.heappush(heap, [distance[nextCity], nextCity])
        if curCity == end:
            break
    return distance[end]

print(dijkstra(start, end))
    
