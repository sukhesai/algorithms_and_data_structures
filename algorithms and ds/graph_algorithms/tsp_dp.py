import math, itertools


def setup(s=0):
    k = 1 << s
    for i in range(n):
        if i == s:
            continue
        dp[i][ k | (1 << i)] = m[s][i]


def get_multiset(r,n):
    for positions in itertools.combinations(range(n),r):
        ans = 0
        for i in positions:
            ans = ans | (1 << i)
        yield ans


def notin(subset, i):
    return subset & (1 << i) != (1 << i)


def solve(s=0):
    for r in range(3, n+1):
        for subset in get_multiset(r, n):
            if notin(subset, s):
                continue
            for nxt in range(n):
                if nxt == s or notin(subset, nxt):
                    continue
                last_state = subset ^ (1 << nxt)
                for last_node in range(n):
                    if s == last_node or last_node == nxt or notin(subset, last_node):
                        continue
                    newdistance = dp[last_node][last_state] + m[last_node][nxt]
                    if newdistance < dp[nxt][subset]:
                        dp[nxt][subset] = newdistance


def optimal_path(s=0):
    path = [None]*(n+1)
    last_node = s
    last_state = (1 << n) - 1
    for i in range(n-1, 0, -1):
        mincost = math.inf
        for j in range(n):
            if j == s or notin(last_state, j):
                continue
            new_last_state = last_state ^ (1 << j)
            if mincost > dp[j][last_state] + m[j][last_node]:
                curr_node = j
                nn_last_state = new_last_state
                mincost = dp[j][last_state] + m[j][last_node]
        last_node = curr_node
        last_state = nn_last_state
        path[i] = last_node
    path[0] = path[-1] = s
    return path


def mincost(s=0):
    cost = math.inf
    fullset = (1 << n) - 1
    for e in range(n):
        if e == s:
            continue
        print(dp[e][fullset], m[e][s])
        cost = min(cost, dp[e][fullset] + m[e][s])
    return cost


m = [[0, 4, 1, 9],
     [3, 0, 6, 11],
     [4, 1, 0, 2],
     [6, 5, -4, 0]]
n = 4
dp = [[math.inf]*(2**n) for i in range(n)]
setup()
solve()
cost = mincost()
path = optimal_path()
print(cost)
print(path)
