import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

def solution():
    arr.sort()
    s = 0
    e = arr[-1]
    answer = 0
    while s<e:
        m = (s+e)//2    
        temp = 0
        for elem in arr:
            if elem > m:
                temp += elem-m
        if temp >= M:
            answer = max(answer, m)
            s = m+1
        else:
            e = m
    return answer

print(solution())

