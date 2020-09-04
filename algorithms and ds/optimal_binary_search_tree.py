import math


def optimal_cost():
    n = len(p)
    w = [[] for _ in range(n)]
    for i in range(n):
        w[i].append(p[i]+q[i]+q[i+1])
        for j in range(n-i-1):
            w[i].append(w[i][j]+p[i+j+1]+q[i+j+2])
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return cost(w, dp, 0, n-1)


def cost(w, dp, i, j):
    if i > j:
        return q[i]
    if dp[i][j] != -1:
        return dp[i][j]
    optimal_cost_of_subtree = math.inf
    for r in range(i, j+1):
        optimal_cost_of_subtree = min(optimal_cost_of_subtree,
                                      cost(w, dp, i, r-1) + cost(w, dp, r+1, j)
                                      + w[i][j-i])
    dp[i][j] = optimal_cost_of_subtree
    return optimal_cost_of_subtree


p = [0.15, 0.10, 0.05, 0.10, 0.20]
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
print(optimal_cost())
