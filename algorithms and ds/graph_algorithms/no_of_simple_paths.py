

def dfs(i):
    if i == end:
        return 1
    discovered[i] = True
    paths = 0
    for next_node in g[i]:
        if not discovered[next_node]:
            paths += dfs(next_node)
        elif processed[next_node]:
            paths += paths_from[next_node]
    processed[i] = True
    paths_from[i] = paths
    return paths


g = [[1, 2, 8],
     [3],
     [3, 4],
     [5],
     [5, 6, 1],
     [7],
     [7, 3, 4],
     [0],
     [9, 10],
     [],
     [2]]
end = 7
discovered = [False]*11
processed = [False]*11
paths_from = [0]*11
print(dfs(0))
