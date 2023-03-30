import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
parents = [i for i in range(N+1)]
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split(' '))))
edges.sort(key=lambda x: x[2])


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def kruskal():
    total_cost = 0
    connected_edges = 0
    for [n1, n2, w] in edges:
        if connected_edges == N-2:
            break
        if find(n1) != find(n2):
            union(n1, n2)
            total_cost += w
            connected_edges += 1
    return total_cost

print(kruskal())