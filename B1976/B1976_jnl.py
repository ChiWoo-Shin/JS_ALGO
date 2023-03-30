import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parents = [i for i in range(N+1)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(N):
    arr = list(map(int, input().split(' ')))
    for j in range(i+1, N):
        if arr[j] == 1:
            union(i+1, j+1)

plans = list(map(int, input().split(' ')))

def solution():
    for i in range(M-1):
        if find(plans[i]) != find(plans[i+1]):
            return 'NO'
    return 'YES'

print(solution())