def LCS(i, j, dp):

    if i == -1 or j == -1:
        return ""

    if dp[i][j] != 0:
        return dp[i][j]

    if X[i] == Y[j]:

        dp[i][j] = LCS(i-1, j-1, dp) + X[i]
        return dp[i][j]

    lcs1 = LCS(i, j-1, dp)
    lcs2 = LCS(i-1, j, dp)

    if len(lcs1) >= len(lcs2):
        dp[i][j] = lcs1
        return lcs1
    else:
        dp[i][j] = lcs2
        return lcs2


X = 'character'
Y = X[::-1]
m = len(X)
n = len(Y)
dp = [[0]*n for _ in range(m)]
lcs = LCS(m-1, n-1, dp)
print(lcs)
