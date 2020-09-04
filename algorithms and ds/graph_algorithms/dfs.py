

def dfs(i):
    global time
    print('present node:', i)
    time += 1
    discover_time[i] = time
    for next_node in g[i]:
        if discover_time[next_node] is None:
            parent[next_node] = i
            tree_edges.append((i, next_node))
            dfs(next_node)
        elif processed[next_node] is None:
            back_edges.append((i, next_node))
        else:
            if discover_time[i] < discover_time[next_node]:
                forward_edges.append((i, next_node))
            else:
                cross_edges.append((i, next_node))

    time += 1
    processed[i] = time


g = [[2, 5, 3, 1],
     [0, 3, 6, 4],
     [0, 5],
     [0, 1, 5, 6],
     [1, 6],
     [2, 0, 3, 6],
     [5, 3, 1, 4]]
time = 0
n = len(g)
discover_time = [None]*n
processed = [None]*n
parent = [None]*n
back_edges = []
tree_edges = []
forward_edges = []
cross_edges = []
dfs(0)
print('discover time:', discover_time)
print('processed', processed)
print('parent', parent)
print('back', back_edges)
print('tree', tree_edges)
print('forward', forward_edges)
print('cross', cross_edges)
