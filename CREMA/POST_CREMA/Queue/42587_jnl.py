from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append([value, idx])
    
    cnt = 0
    while queue:
        v, i = queue.popleft()
        if queue:
            maxV = max(queue)[0]
            if v >= maxV:
                cnt += 1
                if i == location:
                    break
            else:
                queue.append([v, i])
        else:
            cnt+=1
    return cnt
    