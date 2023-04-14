from collections import deque
def solution(N,A, B):
    queue = deque([i for i in range(1, N+1)])
    m, n = min(A, B), max(A, B)
    
    cnt = 1
    
    length = N
    while len(queue) >= 2:
        a = queue.popleft()
        b = queue.popleft()
        if a == m and b == n:
            break
        elif a == n or a == m:
            queue.append(a)
        elif b == n or b == m:
            queue.append(b)
        else:
            queue.append(a)
        if len(queue) * 2 == length:
            cnt += 1
            length //= 2
    return cnt