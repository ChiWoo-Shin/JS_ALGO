import sys
input = sys.stdin.readline

L, C = map(int, input().split(' '))
arr = list(input().rstrip().split(' '))
v_set = set(['a', 'e', 'i', 'o', 'u'])
v_arr = []
c_arr = []
for char in arr:
    if char in v_set:
        v_arr.append(char)
    else:
        c_arr.append(char)

v_ = set()
s_ = set()
def dfs(flag, curDepth, limitDepth, temp, visited, start):
    if curDepth == limitDepth:
        if flag:
            v_.add(temp)
        else:
            s_.add(temp)
        return
    
    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i] = 1
            if flag:
                dfs(flag, curDepth+1, limitDepth, temp+v_arr[i], visited, i+1)
            else:
                dfs(flag, curDepth+1, limitDepth, temp+c_arr[i], visited, i+1)
            visited[i] = 0




def solution():
    global v_, s_
    result = []
    for i in range(1, L):
        v = i
        c = L-i
        if v >= 1 and c >= 2:
            visited1 = [0] * len(v_arr)
            visited2 = [0] * len(c_arr)
            dfs(1, 0, v, '', visited1, 0)
            dfs(0, 0, c, '', visited2, 0)
            for v_elem in v_:
                for s_elem in s_:
                    result.append(''.join(sorted(list(v_elem+s_elem))))
        v_ = set()
        s_ = set()
    
    result.sort()
    for elem in result:
        print(elem)

solution()


