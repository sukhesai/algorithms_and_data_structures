import math


def optimal_cost(i, j):
    if i == j:
        return 0
    if (i, j) in dp:
        return dp[(i, j)]
    cost = math.inf
    no = 0
    for k in breakpoints:
        if k > j:
            break
        if i < k and k < j:
            no += 1
            new_cost = (j-i) + optimal_cost(i, k) + optimal_cost(k, j)
            if new_cost < cost:
                cost = new_cost

    if no == 0:
        cost = 0
    dp[(i, j)] = cost
    return cost


L = 20
breakpoints = [8, 2, 10]
dp = dict()
print(optimal_cost(0, 20))
