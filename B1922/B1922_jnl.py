import sys, heapq
input = sys.stdin.readline

N = int(input()) # 노드의 개수
M = int(input()) # 간선의 개수

def prim():
    edges = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)] 
    for _ in range(M):
        node1, node2, weight = map(int, input().split(' '))
        edges[node1].append([weight, node2])
        edges[node2].append([weight, node1])
    total_cost = 0

    heap = edges[1]
    heapq.heapify(heap)

    visited[1] = 1
    connected = 1

    while heap:
        if connected == N:
            break
        w, n = heapq.heappop(heap)
        if not visited[n]:
            visited[n] = 1
            total_cost += w
            connected += 1
            for edge in edges[n]:
                heapq.heappush(heap, edge)

    return total_cost

# print(prim())

def find(parents, x):
    if x != parents[x]:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def kruskal():
    total_costs = 0
    connected_edge = 0
    parents = [i for i in range(N+1)]
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split(' '))))
    edges.sort(key=lambda x: x[2])
    for [n1, n2, w] in edges:
        if connected_edge == N-1:
            break
        if find(parents, n1) != find(parents, n2):
            union(parents, n1, n2)
            total_costs += w
            connected_edge += 1
    return total_costs

print(kruskal())


        
    
    
