import math
combi = set()

def dfs(curStep, limit, temp):
    if curStep == limit:
        combi.add(temp)
        return

    for i in range(4):
        dfs(curStep+1, limit, temp+str(i))

def solution(users, emoticons):
    dfs(0, len(emoticons), '')
    
    result = []
    for subArr in combi:
        subArr = list(map(int, subArr))
        temp = [0, 0]
        for [rate, money] in users:
            m = 0
            rate = int((math.ceil(rate*0.1))*10)
            for e_idx, e_rate in enumerate(subArr):
                e_rate = (e_rate+1)*10
                if rate <= e_rate:
                    m += int(emoticons[e_idx] * (100-e_rate) * 0.01)
                    if m >= money:
                        temp[0] += 1
                        break
            if m < money:
                temp[1] += m
        result.append(temp)
    result.sort(reverse=True)
    
    return result[0]