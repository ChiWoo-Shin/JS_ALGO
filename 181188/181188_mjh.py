def solution(targets):
    answer = 1
    
    targets.sort()
    current_end = targets[0][1]
    for s, e in targets:
        if s >= current_end:
            answer += 1
            current_end = e
        if e < current_end:
            current_end = e
    
    return answer
