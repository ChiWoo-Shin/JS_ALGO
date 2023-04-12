def solution(arr):
    stack = [arr.pop()]
    while arr:
        a = arr.pop()
        if a != stack[-1]:
            stack.append(a)
    return list(reversed(stack))
