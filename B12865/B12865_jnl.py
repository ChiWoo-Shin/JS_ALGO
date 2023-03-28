import sys
input = sys.stdin.readline

items = [[0, 0]]
N, K = map(int, input().split(' '))
dp = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    items.append(list(map(int, input().split(' '))))

for i in range(1, N+1):
    w, v = items[i]
    for j in range(1, K+1):
        if j < w: # 가방의 capacity를 넘겨버려서 # 넣을 수가 없음
            dp[i][j] = dp[i-1][j]
        else: # 넣을 수는 있는데 # 넣지 않았을 때의 가치가 더 큰지 # 넣었을 때의 가치가 더 큰지
            # 이게 가능한 이유는 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])

# Fractional Knapsack 문제는 Greedy로 풀 수 있다.
# 0-1 Knapsack 문제는 DP를 사용한다.
# 1) 큰 문제를 작은 문제로 쪼개서 해결
# 2) 이전에 계산해둔 값을 메모리에 저장해서 반복 작업을 줄인다.

# DP를 적용하기 위해서는 '최적의 원리'가 성립하는지 확인해야 한다.
# 최적의 원리: 어떤 문제의 입력 사례의 최적해가 그 입력 사례를 분할한 부분 사례에 대한 최적해를 항상 포함하고 있으면, 그 문제에 대하여 최적의 원리가 성립한다.

# Knapsack에서 최적의 원리
# 집합 A가 n번째 보석을 포함하고 있지 않다면, A는 n번째 보석을 뺀 나머지 n-1개의 보석 중에서 최적으로 고른 부분집합과 같다.
# 집합 A가 n번째 보석으로 포함하고 있다면, A에 속한 보석들의 총 가격은 n-1개의 보석들 중에서 최적으로 고른 가격의 합에다가 보석 n의 가격을 더한 것과 같다.(단, 배낭의 capacity를 넘기면 안된다.)