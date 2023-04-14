MAX_INF = float('inf')
MIN_INF = float('-inf')
def solution(line):
    points = set()
    N = len(line)
    for i in range(1, N):
        for j in range(i):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d-b*c == 0:
                continue
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)
            if x == int(x) and y == int(y):
                points.add((int(x), int(y)))
                
    minX, minY, maxX, maxY = MAX_INF, MAX_INF, MIN_INF, MIN_INF
    
    for (x, y) in points:
        minX, minY = min(x, minX), min(y, minY)
        maxX, maxY = max(x, maxX), max(y, maxY)
    
    width = maxX - minX + 1
    height = maxY - minY + 1
    
    result = [['.']*(width) for _ in range(height)]
    for (x, y) in points:
        x = x - minX
        y = maxY - y
        result[y][x] = '*'
    
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    return result
    
        