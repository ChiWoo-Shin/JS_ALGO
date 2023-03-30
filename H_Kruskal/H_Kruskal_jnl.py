import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskals(g_nodes, g_from, g_to, g_weight):
    parent = [i for i in range(g_nodes+1)]
    edges = []
    total_cost = 0
    for i in range(g_nodes):
        edges.append([g_weight[i], g_from[i], g_to[i]])
        # heapq.heappush(heap, [g_weight[i], g_from[i], g_to[i]])
    edges.sort()
    for i in range(g_nodes):
        # w, s, e = 
        w, s, e = edges[i]

        # 부모 노드가 다르면 사이클 발생하지 않음
        if find_parent(parent, s) != find_parent(parent, e):
            union_parent(parent, s, e)
            print(s, e)
            total_cost += w
    return total_cost

print(kruskals(6, [1, 1, 4, 2, 3, 3], [2, 3, 1, 4, 2, 4], [5, 3, 6, 7, 4, 5]))

    