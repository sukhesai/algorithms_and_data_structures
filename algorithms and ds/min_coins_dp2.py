import math


def coin(n, dp, res):
    dp[0] = 0
    for i in range(1, n+1):
        m = math.inf
        for j in range(t):

            if d[j] <= i and dp[i-d[j]] + 1 < m:
                m = dp[i-d[j]] + 1
                res[i] = j
        dp[i] = m
        


d = [1, 3, 4]
n = 6
t = len(d)
res = [0]*(n+1)
dp = [None]*(n+1)
print(coin(n, dp, res))
print(dp)
i = n
coins = [0]*t
while i > 0:
    coins[res[i]] += 1
    i -= d[res[i]]
print(coins)
