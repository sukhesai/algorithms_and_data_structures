def LCS(m, n):

    for i in range(m):
        a = 0
        for j in range(n):

            temp = dp[j+1]

            if X[i] == Y[j]:
                dp[j+1] = a + 1

            elif dp[j] >= dp[j+1]:
                dp[j+1] = dp[j]

            else:
                pass
            a = temp

    return dp[n]


X = 'adabbabaddfsgdfg'
Y = 'daadddfgdfgfg'
m = len(X)
n = len(Y)
dp = [0]*(n+1)

print(LCS(m, n))
