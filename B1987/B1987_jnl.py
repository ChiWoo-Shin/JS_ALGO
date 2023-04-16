import sys
input = sys.stdin.readline

R, C = map(int, input().split(' '))
matrix = []
for _ in range(R):
    matrix.append(list(input().rstrip()))

def solution():
    queue = set([(matrix[0][0], 0, 0)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maxLength = 1
    while queue:
        alphabets, y, x = queue.pop()
        maxLength = max(maxLength, len(alphabets))
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<C and 0<=ny<R and matrix[ny][nx] not in alphabets:
                queue.add((alphabets+matrix[ny][nx],ny, nx ))
    
    return maxLength

print(solution())