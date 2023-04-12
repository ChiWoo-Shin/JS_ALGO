from collections import defaultdict
result = []

def dfs(visited, limit, temp, graph):
    if all(visited):
        result.append(temp)
        return 
    for [nextCity, tIdx]in graph[temp[-1]]:
        if not visited[tIdx]:
            visited[tIdx] = 1
            dfs(visited, limit, temp+[nextCity], graph)
            visited[tIdx] = 0
    return
        
            
    
def solution(tickets):
    N = len(tickets)
    graph = defaultdict(list)
    for idx, [a, b] in enumerate(tickets):
        graph[a].append([b, idx])  
    
    for [nextCity, tId] in graph['ICN']:
        visited = [0] * N
        visited[tId] = 1
        dfs(visited, N, ['ICN', nextCity],  graph)
    result.sort()
    return result[0]