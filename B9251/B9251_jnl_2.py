#최장 공통 부분 문자열
def subString(word, matrix, y, x):
    result = ''
    while matrix[y][x] > 0:
        result = word[y] + result
        y -= 1
        x -= 1
    return result

def LCString(word1, word2):
    result = [-1, 0, 0]
    N = len(word1)
    M = len(word2)
    LCS = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            else:
                if word1[i] == word2[j]:
                    LCS[i][j] = LCS[i-1][j-1] + 1
                    if result[0] < LCS[i][j]:
                        result = [LCS[i][j], i, j]

                else:
                    LCS[i][j] = 0

    s = subString(word1, LCS, result[0], result[1])
    return result[0], s
    

# print(LCString('ABCDEF', 'GBCDFE'))


# 최장 공통 부분 수열 # 길이 찾기

def subSequence(word, matrix):
    result = ''
    y = len(matrix) - 1
    x = len(matrix[0]) - 1
    
    while y>=0 and x >=0 and matrix[y][x] != 0:
        v = matrix[y][x]
        if matrix[y-1][x] == v:
            y -= 1
        elif matrix[y][x-1] == v:
            x -= 1
        else:
            result = word[y-1] + result
            y -= 1
            x -= 1
    return result


def LCSequence(word1, word2):
    result = -1
    N = len(word1)+1
    M = len(word2)+1
  
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

    # s = subSequence(word1, LCS)
    return result
print(LCSequence('ACAYKP', 'CAPCAK'))