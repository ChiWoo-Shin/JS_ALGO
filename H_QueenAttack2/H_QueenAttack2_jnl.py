def queensAttack(n, k, r_q, c_q, obstacles):
    answer = 0
    
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    s = set()
    for obstacle in obstacles:
        r = n - obstacle[0]
        c = obstacle[1]- 1
        s.add((r, c))
    
    for i in range(8):
        nx = c_q-1+ dx[i]
        ny = n-r_q+dy[i]
        while 0<=nx<n and 0<=ny<n and (ny, nx) not in s:
            s.add((ny, nx))
            answer += 1
            nx += dx[i]
            ny += dy[i]
    return answer