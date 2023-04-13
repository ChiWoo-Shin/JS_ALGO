import sys
input = sys.stdin.readline

word1 = ' '+input().rstrip()
word2 = ' '+input().rstrip()

def solution():
    N = len(word1)
    M = len(word2)

    LCS = [[0]*(M) for _ in range(N)]

    for i in range(1, N):
        for j in range(1, M):
            if word1[i] == word2[j]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    
    return LCS[N-1][M-1]

print(solution())