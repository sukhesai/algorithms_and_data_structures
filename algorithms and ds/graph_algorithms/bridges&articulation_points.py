

def bridges_and_articulation_points():
    low = [None]*n
    ids = [None]*n
    bridges = []
    visited = [False]*n
    id_no = 0
    articulation_points = [False]*n
    for i in range(n):
        if not visited[i]:
            out_edge_count = 0
            id_no = dfs(i, i, -1, id_no, bridges, articulation_points, ids, low, out_edge_count, visited)
            if out_edge_count < 2:
                articulation_points[i] = False
    print(ids)
    return articulation_points, bridges


def dfs(root, curr, parent, id_no, bridges, articulation_points, ids, low, out_edge_count, visited):
    if parent == root:
        out_edge_count += 1
    visited[curr] = True
    ids[curr] = id_no
    id_no += 1
    low[curr] = id_no

    for neighbour in g[curr]:
        if neighbour == parent:
            continue
        if not visited[neighbour]:
            id_no = dfs(root, neighbour, curr, id_no, bridges, articulation_points, ids, low, out_edge_count, visited)
            low[curr] = min(low[curr], low[neighbour])
            if ids[curr] < low[neighbour]:
                bridges.append((curr, neighbour))
                articulation_points[curr] = True
            if ids[curr] == low[neighbour]:
                articulation_points[curr] = True
        else:
            low[curr] = min(low[curr], ids[neighbour])
    return id_no

g = [[1, 2], [0, 3], [0, 3], [1, 2, 4, 7], [3, 5, 6], [4, 6], [4, 5], [3, 8], [7]]
n = 9
print(bridges_and_articulation_points())
