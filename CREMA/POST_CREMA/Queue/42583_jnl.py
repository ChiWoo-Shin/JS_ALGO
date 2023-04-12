from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    queue = deque([0] * bridge_length)
    ready = deque(truck_weights)
    
    time = 0
    sumWeights = 0
    while queue:
        q = queue.popleft()
        sumWeights -= q
        if ready:
            if sumWeights + ready[0] <= weight:
                sumWeights += ready[0]
                queue.append(ready.popleft())
                
            else:
                queue.append(0)
        time += 1
    return time