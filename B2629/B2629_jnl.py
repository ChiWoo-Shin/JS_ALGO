n,k = int(input()),list(map(int,input().split()))
m,l = int(input()),list(map(int,input().split()))

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열을 구성한다.
dp,r = [[0 for j in range((i+1)*500+1)] for i in range(n+1)],[]

def cal(num,weight):
    # 추의 개수별로 만들 수 있는 무게 리스트
    # 같은 추의 개수로 똑같은 무게를 만들었다면 바로 리턴
    if num > n or dp[num][weight]:
        return 
    
    dp[num][weight] = 1 # num개의 추를 저울에 올린 적이 있음을 표시
    
    # ~을 사용해서 : 재귀를 돌면서 
    # ~무게는 만들 수 있어요 : weight
    cal(num+1, weight) # 추를 사용하지 않는다.
    cal(num+1, weight+k[num-1]) # 추의 무게를 더한다
    cal(num+1, abs(weight-k[num-1])) # 추의 무게를 뺀다
    
cal(0,0)

for i in l:
    # 문제의 조건상 아예 만들수 없는 무게이므로
    if i > 30*500:
        r.append("N")
        continue

    if dp[n][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)