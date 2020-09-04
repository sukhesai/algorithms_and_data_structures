import math


def topsort():
    n = len(g)
    V = [False]*n
    res = [None]*n
    i = n - 1
    for at in range(n):
        if not V[at]:
            i = dfs(i, at, V, res)
    return res


def dfs(i, at, V, res):
    V[at] = True
    for next_node in g[at]:
        if not V[next_node[0]]:
            i = dfs(i, next_node[0], V, res)
    res[i] = at
    return i-1


def sssp(res):
    n = len(res)
    sssp_list = [math.inf]*n
    path = [None]*n
    sssp_list[res[0]] = 0
    for i in res:
        print('current node:', i)
        for j in g[i]:
            print('its next node:', j[0])
            if sssp_list[i] + j[1] < sssp_list[j[0]]:
                print('previous cost to reach {} is {}'.format(j[0], sssp_list[j[0]]))
                sssp_list[j[0]] = sssp_list[i] + j[1]
                path[j[0]] = i
                print('updating cost {} to reach {}'.format(sssp_list[j[0]], j[0]))
    return sssp_list, path

g = (((1, 1), (2, 4)), ((3, 1), ), ((4, 2), ), ((2, 1), (5, 2)), (), ((4, 3), ))
res = topsort()
print(res)
sssp_list, path = sssp(res)
print(sssp_list, path)
