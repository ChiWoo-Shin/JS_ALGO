import math

def num_to_bin(digit):
    result = ''
    while digit > 0:
        result = str(digit % 2) + result
        digit //= 2
    return result

def zero_cnt(binary):
    idx = 0
    l = len(binary)
    
    while True:
        if math.pow(2, idx)-1<=l<=math.pow(2, idx+1)-1:
            break
        idx += 1
    return math.pow(2, idx+1)-1-l

flag = True
def dfs(word): 
    global flag
    if len(word) == 3:
        if word[1] == '0':
            if word[0] != '0' or word[2] != '0':
                flag = False
                
        return
        
    idx = len(word)//2
    left = word[:idx]
    right = word[idx+1:]
    
    if word[idx] == '0':
        if left != '0'*len(left) or right != '0'*len(right):
            flag = False
            return
        
    dfs(left)
    dfs(right)

def solution(numbers):
    global flag 
    result = []
    for number in numbers:
        binary = num_to_bin(number)
        binary = '0'*int(zero_cnt(binary)) + binary
        
        if len(binary) < 3:
            if binary == '0':
                result.append(0)
            else:
                result.append(1)    
            continue
            
        dfs(binary)
        
        if flag:
            result.append(1)
        else:
            result.append(0)
        flag = True
    return result
 