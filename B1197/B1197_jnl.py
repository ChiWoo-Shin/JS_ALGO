# 최소 스패닝 트리
# Kruskal
# V, E = map(int, input().split(' '))
# parents = [i for i in range(V+1)]
# edges = []
# for _ in range(E):
#     edges.append(list(map(int, input().split(' '))))
# edges.sort(key=lambda x:x[2])

# def find(x):
#     if x != parents[x]:
#         parents[x] = find(parents[x])
#     return parents[x]

# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b

# def solution():
#     total_costs = 0
#     for [node1, node2, weight] in edges:
#         if find(node1) != find(node2):
#             union(node1, node2)
#             total_costs += weight
#     return total_costs

# print(solution())

#Prim
import sys, heapq
# from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split(' '))
# graph = defaultdict(list)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    node1, node2, weight = map(int, input().split(' '))
    graph[node1].append([weight, node2])
    graph[node2].append([weight, node1])

def solution():
    total_cost = 0
    visited = [0] * (V+1)
    # 임의의 정점: 1
    heap = sorted(graph[1])
    # print(graph[1])
    # heap = [[0, 1]]
    visited[1] = 1
    # print(heap)

    while heap:
        weight, node = heapq.heappop(heap)
        # print('=>', node)
        if not visited[node]:
            # print('->', node)
            visited[node] = 1
            total_cost += weight
            for elem in graph[node]:
                heapq.heappush(heap, elem)
    return total_cost

print(solution())