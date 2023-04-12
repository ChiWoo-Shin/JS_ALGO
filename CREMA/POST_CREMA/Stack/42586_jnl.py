import math
def solution(progresses, speeds):
    N = len(progresses)
    if N == 1:
        return 1
    arr = []
    for i in range(N):
        progress = progresses[i]
        speed = speeds[i]
        arr.append(math.ceil((100-progress)/speed))
    
    stack = [arr[0]]
    cnt = 1
    result = []
    for i in range(1, len(arr)):
        if stack:
            if stack[-1] >= arr[i]:
                cnt += 1
            else:
                stack.pop()
                result.append(cnt)
                cnt = 1
                stack.append(arr[i])
    result.append(cnt)
    return result
                
                
                
    
    