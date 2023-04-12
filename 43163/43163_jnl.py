from collections import defaultdict, deque
INF = float('inf')

def bfs(begin, target, graph, dp):
    queue = deque([begin])
    
    while queue:
        q  = queue.popleft()
        if q == begin:
            for p in graph[q]:
                dp[p] = 1
                queue.append(p)
                if p == target:
                    return dp[p]
        else:
            for p in graph[q]:
                if dp[p] == INF:
                    dp[p] = dp[q]+1
                    queue.append(p)
                    if p == target:
                        return dp[p]
    return 0
def solution(begin, target, words):
    N = len(words)
    
    graph = defaultdict(list)
    dp = dict()
    
    for word in words:
        dp[word] = INF
        
    dp[begin] = 0
    wordLength = len(begin)
    
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(wordLength):
                if words[i][k] == words[j][k]:
                    cnt += 1
            if cnt + 1 == wordLength:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
            
            
    for word in words:
        cnt = 0
        for i in range(len(word)):
            if begin[i] == word[i]:
                cnt += 1
        if cnt + 1 == len(word):
            graph[begin].append(word)
                
    return bfs(begin, target, graph, dp)