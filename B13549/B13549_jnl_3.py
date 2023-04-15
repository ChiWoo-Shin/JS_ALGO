import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split(' '))

def solution():
    heap = []
    heapq.heappush(heap, [0, N])
    dp = [INF] * 100001

    while heap:
        t, p = heapq.heappop(heap)
        if p == M:
            return t
        if p-1 >= 0 and dp[p-1] > t+1:
            dp[p-1] = t+1
            heapq.heappush(heap, [t+1, p-1])

        if p+1 < 100001 and dp[p+1] > t+1:
            dp[p+1] = t+1
            heapq.heappush(heap, [t+1, p+1])
        if p*2 < 100001 and dp[p*2] > t:
            dp[p*2] = t
            heapq.heappush(heap, [t, p*2])
    
        
    
print(solution())