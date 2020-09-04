import math


def coin(i, x, dp, res):
    if dp[i][x] is not None:
        return dp[i][x]
    j = x//d[i]
    m = coin(i-1, x, dp, res)
    if j == 0:
        dp[i][x] = m
        return m
    for k in range(1, j+1):
        if m > coin(i-1, x-k*d[i], dp, res)+k:
            m = coin(i-1, x-k*d[i], dp, res)+k
            res[i] = k
    dp[i][x] = m
    return m


d = [1, 3, 4]
n = 6
res = [0]*len(d)
dp = [[None]*(n+1) for _ in range(len(d))]
for i in range(n+1):
    dp[0][i] = i
for i in range(len(d)):
    dp[i][0] = 0
print(coin(2, n, dp, res))
print(dp) 
print(res)
