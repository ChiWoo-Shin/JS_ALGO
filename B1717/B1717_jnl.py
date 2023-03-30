import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parents, x):
    if x != parents[x]:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def solution():
    N, M = map(int, input().split(' '))
    parents = [i for i in range(N+1)]

    for _ in range(M):
        op, num1, num2 = map(int, input().split(' '))
        if op == 0:
            if num1 == num2:
                continue
            union(parents, num1, num2)
        else:
            if find(parents, num1) != find(parents, num2):
                print('NO')
            else:
                print('YES')

solution()