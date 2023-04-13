from collections import defaultdict

word1 = input()
word2 = input()
D1 = defaultdict(set)

FLAG = False
def dfs(curStep, limit, flag, temp, visited, start):
    global FLAG
    if curStep == limit:
        if flag == 1:
            D1[limit].add(temp)
        else:
            if temp in D1[limit]:
                FLAG = True
        return

    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i] = 1
            if flag == 1:
                dfs(curStep+1, limit, flag, temp+word1[i], visited,start+1)
            else:
                dfs(curStep+1, limit, flag, temp+word2[i], visited,start+1)
            visited[i] = 0

def solution():
    global FLAG
    maxLength = min(len(word1), len(word2))
    for l in range(maxLength, 0, -1):
        visited1 = [0] * len(word1)
        visited2 = [0] * len(word2)
        dfs(0, l, 1, '', visited1, 0)
        dfs(0, l, 2, '', visited2, 0)
        
        if FLAG:
            return l

print(solution())