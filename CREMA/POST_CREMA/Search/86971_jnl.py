from collections import defaultdict, deque

def bfs(n1, n2, graph, n):
    queue = deque([n1])
    visited = [0]*(n+1)
    cnt = 0
    while queue:
        q = queue.popleft()
        if not visited[q]:
            visited[q] = 1
            cnt += 1
            for p in graph[q]:
                if q == n1 and p == n2:
                    continue
                else:
                    queue.append(p)
    return cnt
    
def solution(n, wires):
    minAbs = n
    graph = defaultdict(list)
    for [a, b] in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for [a, b] in wires:
        result = bfs(a, b, graph, n)
        temp = abs(result - n + result)
        minAbs = min(minAbs, temp)
    return minAbs