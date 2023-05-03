def nonDivisibleSubset(k, s):
    counter = [0] * k
    for elem in s:
        counter[elem%k] += 1
    
    answer = 0
    if counter[0] > 0:
        answer = 1
    for i in range(1, k//2):
        answer += max(counter[i], counter[k-i])
    if k % 2 == 0:
        if counter[k//2] > 0: 
            answer += 1
    elif k != 1:
        answer += max(counter[k//2], counter[(k//2)+1])
    return answer 
        
print(nonDivisibleSubset(4, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))