import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))

maxV = float('-inf')
minV = float('inf')

def eval(op, a, b):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        if a < 0:
            return -(abs(a)//b)
        else:
            return a//b


def dfs(cur, limit, temp, arr):
    global minV, maxV
    if cur == limit:
        minV = min(temp, minV)
        maxV = max(temp, maxV)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            result = eval(i, temp, arr[cur])
            dfs(cur+1, limit, result, arr)
            op[i] += 1

def solution():
    dfs(1, N, arr[0], arr)
    print(maxV, minV, sep='\n')
solution()