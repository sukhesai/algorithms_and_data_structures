import math


def floyd_warshall():
    dp = [[math.inf]*V for i in range(V)]
    next_ = [[None]*V for i in range(V)]
    setup(dp, next_)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_[i][j] = next_[i][k]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = -math.inf
                    next_[i][j] = -1

    return dp, next_


def setup(dp, next_):
    for i in range(V):
        for j in range(V):
            if M[i][j] is not None:
                dp[i][j] = M[i][j]
                next_[i][j] = j


M = [[None, 5, None, 10],
     [None, None, 3, None],
     [None, None, None, 1],
     [None, None, None, None]]
V = 4

print(floyd_warshall())
