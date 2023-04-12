import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

result = []
def dfs(visited, cur, limit, temp):
    if cur == limit:
        result.append(temp)
        return
    
    for i in range(1, len(visited)):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, cur+1, limit, temp+[i])
            visited[i] = 0



def solution():
    for i in range(1, N+1):
        visited = [0] * (N+1)
        visited[i] = 1
        dfs(visited, 1, M, [i])
    
    for pair in result:
        print(*pair)
    
solution()



