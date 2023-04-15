import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = defaultdict(list)

for _ in range(M):
    n1, n2, c = map(int, input().split(' '))
    graph[n1].append([c, n2])

src, dest = map(int, input().split(' '))

def solution():
    dist = [INF] * (N+1)
    heap = [[0, src]]

    while heap:
        c, n = heapq.heappop(heap)
        for [c_, n_] in graph[n]:
            if dist[n_] > c + c_:
                dist[n_] = c+c_
                heapq.heappush(heap, [dist[n_], n_])
        if n == dest:
            break
    
    return dist[dest]

print(solution())