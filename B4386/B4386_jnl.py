import sys, math
input = sys.stdin.readline
N = int(input())
points = []
parents = [i for i in range(N+1)]
for _ in range(N):
    points.append(list(map(float, input().split(' '))))
edges = []
for i in range(N):
    p1 = points[i]
    for j in range(i+1, N):
        p2 = points[j]
        w = abs(p1[0]-p2[0]) ** 2 + abs(p1[1]-p2[1])**2
        edges.append([w, i, j])
edges.sort()

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

def kruskal():
    total_costs = 0
    connected_edges = 0
    for [w, p1, p2] in edges:
        if connected_edges == N-1:
            break
        if find(p1) != find(p2):
            union(p1, p2)
            total_costs += int(math.sqrt(w) * 100) * 0.01
            connected_edges+= 1
    return total_costs
    

print(kruskal())



