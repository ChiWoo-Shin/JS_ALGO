cnt = 0
def dfs(numbers, cur, temp, target):
    global cnt
    if cur == len(numbers):
        if temp == target:
            cnt += 1
        return
    dfs(numbers, cur+1, temp+numbers[cur], target)
    dfs(numbers, cur+1, temp-numbers[cur], target)
    

def solution(numbers, target):
    global cnt
    dfs(numbers, 1, numbers[0], target)
    dfs(numbers, 1, -numbers[0], target)
    return cnt
    