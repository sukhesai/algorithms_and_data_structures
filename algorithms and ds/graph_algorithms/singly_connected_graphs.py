

def dfs(i, time):
    seen[i] = time
    time += 1
    for neighbour in g[i]:
        if seen[neighbour] is None:
            tree_edges.append((i, neighbour))
            time = dfs(neighbour, time)
        elif finished[neighbour] is None:
            back_edges.append((i, neighbour))
        else:
            if seen[neighbour] > seen[i]:
                forward_edges.append((i, neighbour))
            else:
                cross_edges.append((i, neighbour))
    finished[i] = time
    time += 1
    return time


g = [[2, 5, 3, 1],
     [0, 3, 6, 4],
     [0, 5],
     [0, 1, 5, 6],
     [1, 6],
     [2, 0, 3, 6],
     [5, 3, 1, 4]]
n = len(g)
time = 0
seen = [None]*n
finished = [None]*n
reachable = [0]*n
back_edges = []
tree_edges = []
forward_edges = []
cross_edges = []
for i in range(n):
    if not seen[i]:
        cycles = []
        time = dfs(i, time)
    for cycle in cycles:
        
print('discover time:', seen)
print('processed time', finished)
print('back', back_edges)
print('tree', tree_edges)
print('forward', forward_edges)
print('cross', cross_edges)
