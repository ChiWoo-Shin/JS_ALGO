from collections import deque, defaultdict

blocks = defaultdict(list)
puzzles = defaultdict(list)

def bfs(N,game_board, y, x, empty):
    queue = deque([[y, x]])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    temp = []
    while queue:
        y, x = queue.popleft()
        if game_board[y][x] == empty:
            game_board[y][x] = 1-empty
            temp.append(y*N+x)
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0<=nx<N and 0<=ny<N:
                    if game_board[ny][nx] == empty:
                        queue.append([ny, nx])
    
    matrix = makeSquare(temp, N)

    if empty == 0:
        blocks[len(temp)].append(matrix)
    else:
        puzzles[len(temp)].append(matrix)
        
def makeSquare(arr, N):
    minV = [N, N] #x좌표, y좌표
    maxV = [0, 0] #x좌표, y좌표
    for elem in arr:
        y, x = elem // N, elem % N
        minV[0] = min(minV[0], x)
        minV[1] = min(minV[1], y)
        
        maxV[0] = max(maxV[0], x)
        maxV[1] = max(maxV[1], y)
    width = maxV[0] - minV[0] + 1
    height = maxV[1] - minV[1] + 1
    
    matrix = [[0]*width for _ in range(height)]
    for elem in arr:
        y, x = elem // N, elem % N 
        matrix[y-minV[1]][x-minV[0]] = 1
    return matrix
        
def spin(arr, N):
    result = []
    for i in range(4):
        n = len(arr)
        m = len(arr[0])
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][n-i-1] = arr[i][j]
        result.append(new)
        arr = new
    return result  

def compare(arr1, arr2, N):
    candidates = spin(arr2,N)
    for candidate in candidates:
        flag = True
        if len(arr1) != len(candidate) or len(arr1[0]) != len(candidate[0]):
            continue
        for y in range(len(arr1)):
            for x in range(len(arr1[0])):
                if arr1[y][x] == candidate[y][x]:
                    continue
                else:
                    flag = False
                    break
        if flag:
            return True 
    return False
    
def solution(game_board, table):
    N = len(game_board)
    # game_board에서 빈칸인 부분 찾기
    for y in range(N):
        for x in range(N):
            if game_board[y][x] == 0:
                bfs(N, game_board, y, x, 0)
    
    # table에서 빈칸인 부분 찾기
    for y in range(N):
        for x in range(N):
            if table[y][x] == 1:
                bfs(N, table, y, x, 1)
    
    cnt = 0
    for key in blocks:
        for arr1 in blocks[key]:
            for arr2 in puzzles[key]:
                if compare(arr1, arr2, N):
                    cnt += key
                    puzzles[key].remove(arr2)
                    break
    return cnt