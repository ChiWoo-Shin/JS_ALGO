def flatlandSpaceStations(n, c):
    if len(c) == n:
        return 0
    elif len(c) == 1:
        answer = 0
        for i in range(n):
            answer = max(answer, abs(c[0]-i))
        return answer
    else:
        c.sort()
        answer = 0
        left = c[0]
        for i in range(1, len(c)):
            answer = max(answer, (left+c[i])//2 - left)
            left = c[i]
        answer = max(answer, abs(n-1-c[-1]))
        answer = max(answer, c[0])
        return answer
    

print(flatlandSpaceStations(10, [0, 5]))