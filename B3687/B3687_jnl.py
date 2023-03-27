import sys
input = sys.stdin.readline
T = int(input())
arr = [[], [], [1], [7], [4], [2,5], [0, 6, 9], [8]]

# DP 테이블 만들기
dp = [[] for _ in range(101)]
dp[2] = [1]
dp[3] = [7]
dp[4] = [4, 11]
for i in range(5, 101):
    if i < 8:
        dp[i] = arr[i]
    for j in range(2, (i//2)+2):
        arr1 = dp[j]
        arr2 = dp[i-j]
        minValue = 0
        maxValue = 0
    
        if (arr1[0] == 0 and arr2[0] == 0):
            minValue = min([arr1[1]*10, arr2[1]*10, int(str(arr1[1])+str(arr2[1])), int(str(arr2[1])+str(arr1[1]))])
        elif (arr1[0] == 0):
            minValue = min([arr2[0]*10, int(str(arr2[0])+str(arr1[1])), int(str(arr1[1])+str(arr2[0]))])
        elif (arr2[0] == 0):
            minValue = min([arr1[0]*10, int(str(arr1[0])+str(arr2[1])), int(str(arr2[1])+str(arr1[0]))])
        else:
            minValue = min([int(str(arr1[0]) + str(arr2[0])), int(str(arr2[0]) + str(arr1[0]))])
        
        if (str(arr1[-1]) > str(arr2[-1])):
            maxValue = int(str(arr1[-1]) + str(arr2[-1]))
        else:
            maxValue = int(str(arr2[-1]) + str(arr1[-1]))
        dp[i].append(minValue)
        dp[i].append(maxValue)
        
    dp[i].sort()

for _ in range(T):
    n = int(input())
    if (dp[n][0] == 0):
        print(dp[n][1], dp[n][-1])
    else:
        print(dp[n][0], dp[n][-1])
    
        


        