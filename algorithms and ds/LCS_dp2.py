def LCS(m, n):

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            elif dp[i+1][j] >= dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
                dir[i][j] = 1
            else:
                dp[i+1][j+1] = dp[i][j+1]
                dir[i][j] = 2

    return make_lcs(m-1, n-1)


def make_lcs(i, j):
    if i < 0 or j < 0:
        return ""
    elif dir[i][j] == 0:
        return make_lcs(i-1, j-1) + X[i]
    elif dir[i][j] == 1:
        return make_lcs(i, j-1)
    return make_lcs(i-1, j)


X = 'adabbabaddfsgdfgasdhfgaygcbreufgycbhrfgygerhedfhvbrgyfcbhdfsjhjhbfhrfgy'
Y = 'daadddfgdfgfgsdfdhsfhfuhruhvrugyfghuhaeygfbcjhbfgvedhsajdfkjuhafurihieuhj'
m = len(X)
n = len(Y)
dir = [[0]*(n) for _ in range(m)]
dp = [[0]*(n+1) for _ in range(m+1)]
lcs = LCS(m, n)
print(lcs)
