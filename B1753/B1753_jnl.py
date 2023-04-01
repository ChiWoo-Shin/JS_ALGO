import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split(' '))
distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
start = int(input())

for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [distance[start], start])

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            temp = dist + next_dist
            if temp < distance[next_node]:
                distance[next_node] = temp
                heapq.heappush(heap, [distance[next_node], next_node])
 
dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(str(distance[i]))