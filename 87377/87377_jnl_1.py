def solution(line):
    N = len(line)
    arr = set()
    for i in range(1, N):
        for j in range(i):
            if i == j: continue
            x = 0.5
            y = 0.5
            a, b, c = line[i]
            aa, bb, cc = line[j]
            
            if a != 0 and aa != 0:
                ta = a
                taa = aa
                a, b, c = a*taa, b *taa, c*taa
                aa, bb, cc = aa*ta, bb *ta, cc*ta
                if (b-bb) == 0:
                    continue
                y = (cc- c)/(b-bb)
                x = (-b*y - c)/a
            elif b != 0 and bb != 0:
                tb = b
                tbb = bb
                a, b, c = a*tbb, b *tbb, c*tbb
                aa, bb, cc = aa*tb, bb *tb, cc*tb
                
                if (a-aa) == 0 or b == 0:
                    continue
                x = (cc-c)/(a-aa)
                if b != 0:
                    y = (-a*x - c)/b
                else:
                    y = (-aa*x-c)/bb
            else:
                if a == 0 and aa != 0 and b!= 0:
                    y = (-c)/b
                    x = (-cc)/aa
                elif a != 0 and aa == 0 and bb != 0:
                    y = (-cc)/bb
                    x = (-c)/a  
                
            if (x == int(x) and y == int(y)):
                arr.add((x, y))     
    arr = list(arr)
    minX, minY = float('inf'), float('inf')
    maxX, maxY = float('-inf'),float('-inf')
    for [x, y] in arr:
        minX, minY = min(minX, x), min(minY, y)
        maxX, maxY = max(maxX, x), max(maxY, y)
    width = int(maxX - minX + 1)
    height = int(maxY - minY + 1)
    
    matrix = [['.']*width for _ in range(height)]
    minX = int(minX)
    maxY = int(maxY)
    
    for [x, y] in arr:
        x = int(x)-minX
        y = maxY-int(y) 
        matrix[y][x] = '*'

    result = []
    for subArr in matrix:
        result.append(''.join(subArr))
    return result
        