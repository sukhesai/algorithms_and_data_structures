def LCS(i, j):
    if i == -1 or j == -1:
        return ""
    if X[i] == Y[j]:
        return LCS(i-1, j-1) + X[i]
    lcs1 = LCS(i, j-1)
    lcs2 = LCS(i-1, j)
    if len(lcs1) >= len(lcs2):
        return lcs1
    else:
        return lcs2


X = 'abcbdd'
Y = 'bdcabadkll'
m = len(X)
n = len(Y)
lcs = LCS(m-1, n-1)
print(lcs)
