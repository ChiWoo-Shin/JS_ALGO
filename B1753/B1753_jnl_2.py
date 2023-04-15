import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split(' '))
start = int(input())
graph = defaultdict(list)
for _ in range(E):
    n1, n2, w = map(int, input().split(' '))
    graph[n1].append([w, n2])
def solution():
    dist = [INF]*(V+1)
    heap = [[0, start]]
    dist[start] = 0
    
    while heap:
        w_, n_ = heapq.heappop(heap)
        if dist[n_] < w_:
            continue
        for [new_w, new_n] in graph[n_]:
            temp_w = new_w + w_
            if temp_w < dist[new_n]:
                dist[new_n] = temp_w
                heapq.heappush(heap, [temp_w, new_n])

    for i in range(1, V+1):
        if dist[i]== INF:
            print('INF')
        else:
            print(dist[i])

solution()