from collections import defaultdict, deque
def bfs(visited, graph, n, cur):
    queue = deque([cur])
    
    while queue:
        q = queue.popleft()
        if not visited[q]:
            visited[q] = 1
            for p in graph[q]:
                queue.append(p)


def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    visited = [0] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(visited, graph, n, i)
            cnt += 1
    return cnt