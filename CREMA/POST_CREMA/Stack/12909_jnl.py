def solution(s):
    if len(s) % 2:
        return False
    
    arr = list(s)
    stack = [arr.pop()]
    while arr:
        a = arr.pop()
        if not stack:
            stack.append(a)
            continue
        if a == '(':
            if stack[-1] == ')':
                stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)
    if stack:
        return False
    else:
        return True