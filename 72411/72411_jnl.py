from collections import defaultdict
D = defaultdict(int)
L = defaultdict(set)
s = set()
def dfs(curStep, limit, visited, temp, word, start):
    if curStep == limit:
        w = ''.join(sorted(temp))
        if w not in s:
            D[w] += 1
            s.add(w)
        L[len(w)].add(w)
        return

    for i in range(start, len(word)):
        if not visited[i]:
            visited[i] = 1
            dfs(curStep+1, limit, visited, temp+word[i], word, start+1)
            visited[i] = 0


def solution(orders, course):
    global s
    for order in orders:
        for c in course:
            visited = [0] * len(order)
            dfs(0, c, visited, '', order, 0)
            s = set()
            
    result = []
    for c in course:
        maxCnt = 0
        maxWord = []
        for key in L[c]:
            if D[key] > maxCnt:
                maxWord = [key]
                maxCnt = D[key]
            elif D[key] == maxCnt:
                maxWord.append(key)
        if maxCnt > 1:
            result += maxWord
    result.sort()
    return result