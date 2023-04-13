word1 = input()
word2 = input()

def solution():
    result = -1
    N = len(word1) + 1
    M = len(word2) + 1

    LCS = [[-1]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            else:
                if word1[i-1] == word2[j-1]:
                    LCS[i][j] = LCS[i-1][j-1] + 1
                    result = max(result, LCS[i][j])
                else:
                    LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    
    return result

print(solution())