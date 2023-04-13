import sys
input = sys.stdin.readline

L, C = map(int, input().split(' '))
arr = list(input().rstrip().split(' '))
vowels = set(['a', 'e', 'i', 'o', 'u'])
arr1 = []
arr2 = []
for char in arr:
    if char in vowels:
        arr1.append(char)
    else:
        arr2.append(char)

s1 = []
s2 =[]
def dfs(arr, visit, curStep, limit, temp, start, flag):
    if curStep == limit:
        if flag == 1:
            s1.append(temp)
        else:
            s2.append(temp)
        return
    for i in range(start, len(visit)):
        if not visit[i]:
            visit[i] = 1
            dfs(arr, visit, curStep+1, limit, temp+arr[i], i+1, flag)
            visit[i] = 0

def solution():
    global s1, s2
    result = set()
    for i in range(1, L+1):
        v = i
        c = L-v
        if v >= 1 and c >= 2 and len(arr1)>=v and len(arr2) >=c:
            visited2 = [0] * len(arr2)
            for i in range(len(arr1)):
                visited1 = [0] * len(arr1)
                visited1[i] = 1
                dfs(arr1, visited1, 1, v, arr1[i], i, 1)
            for i in range(len(arr2)):
                visited2 = [0] * len(arr2)
                visited2[i] = 1
                dfs(arr2, visited2, 1, c, arr2[i], i, 2)
        
        for elem1 in s1:
            for elem2 in s2:
                result.add(''.join(sorted(elem1+elem2)))
        s1 = []
        s2 = []
    result = list(result)
    result.sort()
    for elem in result:
        print(elem)


solution()
    